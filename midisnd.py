
from midi import *
import struct

BLANK = ("Acoustic Grand Piano", [])

def sustain(num_samples, pitch):
	return [pitch * 2] * num_samples

def silence(num_samples):
	return [0] * num_samples

def ramp(num_samples, start, end):
	start *= 2
	end *= 2
	return [
		(end * i + start * (num_samples - 1 - i)) / (num_samples - 1)
		for i in range(num_samples)
	]

def modulate(samples, mod_length):
	result = []
	for idx, s in enumerate(samples):
		if ((idx / mod_length) % 2) == 0:
			result.append(0)
		else:
			result.append(s)
	return result

OUTPUT = {
	"oof": ("Trumpet", ramp(20, On3.C, On4.C)),
	"noway": ("Trumpet", ramp(20, On3.C, On4.C)),
	"wpnup": ("Woodblock",
		sustain(10, On5.Cs) + silence(20) +
		sustain(5, On5.E)),
	"itemup": ("Blown Bottle",
		sustain(10, On3.G) + silence(5) + sustain(10, On3.G)),

	"pistol": ("Gunshot", sustain(50, O3.C)),
	"shotgn": ("Slap Bass 1", ramp(10, On5.B, On5.E)),
	"plasma": ("Trumpet", ramp(70, On2.C, O1.Gs)),

	# Super shotgun
	"dshtgn": ("Slap Bass 1", ramp(15, On5.G, On5.D)),
	"dbopn": BLANK,
	"dbcls": BLANK,
	"dbload": BLANK,

	# Rocket launcher
	"rlaunc": ("Trumpet", ramp(30, On2.B, On4.C)),
	"rxplod": ("Trumpet", ramp(30, On4.C, On4.B)),
	"barexp": ("Trumpet", ramp(30, On4.C, On4.B)),

	# Chainsaw
	"sawup": ("Woodblock", modulate(ramp(30, On5.C, On3.C), 2)),
	"sawidl": ("Woodblock", modulate(sustain(30, On5.G), 2)),
	"sawful": ("Woodblock", modulate(sustain(30, On4.C), 2)),
	"sawhit": ("Woodblock", modulate(sustain(30, On4.E), 2)),

	"podth1": ("Voice Oohs",
		ramp(40, On3.C, On4.C) +
		sustain(20, On4.C) +
		ramp(40, On4.C, On5.D)
	),
	"podth2": ("Voice Oohs",
		ramp(40, On3.E, On5.D)
	),
	"podth3": ("Voice Oohs",
		sustain(20, On4.G) +
		ramp(40, On4.G, On5.D)
	),

	# Switches and doors
	"swtchn": ("Taiko Drum", sustain(50, On1.D)),
	"swtchx": ("Taiko Drum", sustain(50, O0.Ds)),
	"doropn": ("Whistle", ramp(50, On3.C, O0.C)),
	"dorcls": ("Whistle", ramp(30, On2.C, On3.C)),
	"bdopn": ("Whistle", ramp(25, On3.C, O0.C)),
	"bdcls": ("Whistle", ramp(15, On2.C, On3.C)),
	"pstart": ("Trumpet", ramp(25, On4.C, On1.C)),
	"pstop": ("Trumpet", ramp(15, On3.C, On4.C)),

	# TODO
	"sgcock": BLANK,
	"bfg": BLANK,
	"firsht": BLANK,
	"firxpl": BLANK,
	"stnmov": BLANK,
	"plpain": BLANK,
	"dmpain": BLANK,
	"popain": BLANK,
	"vipain": BLANK,
	"mnpain": BLANK,
	"pepain": BLANK,
	"slop": BLANK,
	"telept": BLANK,
	"posit1": BLANK,
	"posit2": BLANK,
	"posit3": BLANK,
	"bgsit1": BLANK,
	"bgsit2": BLANK,
	"sgtsit": BLANK,
	"cacsit": BLANK,
	"brssit": BLANK,
	"cybsit": BLANK,
	"spisit": BLANK,
	"bspsit": BLANK,
	"kntsit": BLANK,
	"vilsit": BLANK,
	"mansit": BLANK,
	"pesit": BLANK,
	"sklatk": BLANK,
	"sgtatk": BLANK,
	"skepch": BLANK,
	"vilatk": BLANK,
	"claw": BLANK,
	"skeswg": BLANK,
	"pldeth": BLANK,
	"pdiehi": BLANK,
	"bgdth1": BLANK,
	"bgdth2": BLANK,
	"sgtdth": BLANK,
	"cacdth": BLANK,
	"skldth": BLANK,
	"brsdth": BLANK,
	"cybdth": BLANK,
	"spidth": BLANK,
	"bspdth": BLANK,
	"vildth": BLANK,
	"kntdth": BLANK,
	"pedth": BLANK,
	"skedth": BLANK,
	"posact": BLANK,
	"bgact": BLANK,
	"dmact": BLANK,
	"bspact": BLANK,
	"bspwlk": BLANK,
	"vilact": BLANK,
	"punch": BLANK,
	"hoof": BLANK,
	"metal": BLANK,
	"chgun": BLANK,
	"tink": BLANK,
	"itmbk": BLANK,
	"flame": BLANK,
	"flamst": BLANK,
	"getpow": BLANK,
	"bospit": BLANK,
	"boscub": BLANK,
	"bossit": BLANK,
	"bospn": BLANK,
	"bosdth": BLANK,
	"manatk": BLANK,
	"mandth": BLANK,
	"sssit": BLANK,
	"ssdth": BLANK,
	"keenpn": BLANK,
	"keendt": BLANK,
	"skeact": BLANK,
	"skesit": BLANK,
	"skeatk": BLANK,
	"radio": BLANK,
}

def encode_sound(instrument, samples):
	# Always turn the sound off at the end.
	samples += [0]
	result = struct.pack("<HHHH", 1, len(samples), 0, instrument)
	for s in samples:
		result += struct.pack("B", s)
	return result

def write_samples(data):
	for name, (instr_name, samples) in data.items():
		instr_index = INSTRUMENTS.index(instr_name)
		assert instr_index >= 0, "unknown instrument '%s'" % instr_name
		encoded = encode_sound(instr_index, samples)
		with open("lumps/%s.lmp" % name, "w") as f:
			f.write(encoded)

def write_config(filename, data):
	with open(filename, "w") as f:
		f.write("[lumps]\n")
		for name in data.keys():
			f.write("da%s = %s\n" % (name, name))
			f.write("dm%s = %s\n" % (name, name))


write_samples(OUTPUT)
write_config("wadinfo.txt", OUTPUT)

