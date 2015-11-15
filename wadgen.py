
import hashlib
import struct

class WadGenerator(object):
	def __init__(self, filename, wad_type="PWAD"):
		# Open file and write initial header.
		self.output = open(filename, "w")
		self.output.write(struct.pack("<4sII", wad_type, 0, 0))

		self.data_offsets = {}
		self.directory = []

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		self.close()

	def add(self, name, data):
		"""Add a lump to the generated WAD."""
		assert self.output is not None
		digest = hashlib.sha1(data).hexdigest()
		if digest not in self.data_offsets:
			self.data_offsets[digest] = self.output.tell()
			self.output.write(data)

		name = name[0:8].upper()
		offset = self.data_offsets[digest]
		self.directory.append((offset, len(data), name))

	def _write_directory(self):
		"""Write the WAD directory to the output file."""
		dir_offset = self.output.tell()
		for entry in self.directory:
			self.output.write(struct.pack("<II8s", *entry))

		# Go back and rewrite the file header with directory info.
		self.output.seek(4)
		self.output.write(struct.pack("<II", len(self.directory),
		                              dir_offset))

	def close(self):
		"""Finish writing and close the file."""
		if self.output is not None:
			self._write_directory()
			self.output.close()
			self.output = None

