from string import *
def gc_counter (seq):
	nbre_c = count(seq, "c")
	nbre_g = count(seq, "g")
	long_seq =len(seq)
	gc_percent =100*float(nbre_c + nbre_g)/long_seq
	return gc_percent
gc= gc_counter ("atgcggctgtgatgtagtcctttc")
print gc
seq= raw_input ("enter a dna sequence: ")
print gc_counter(seq)