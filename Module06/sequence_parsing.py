from Bio import SeqIO
# import the Bio.SeqIO to provide a sample unique interface for the input and output assorted the sequence file

from Bio.SeqRecord import SeqRecord

import os
# import the os modules


# print the header
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('****************                 ')
print('       Sequences Paring APP      ')
print('                *****************')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def get_genbank_path(): # use the function to obtain the file's path and load the file

    filename = None
    while filename is None: # asking the user to input the filename

        filename = input('What is the /path/to/the/genbank/file? ')

        # Check if the filename exists, if not asking the user to try again
        if not os.path.exists(filename):
            print('That file could not be found. Please try again.')
            filename = None

    return filename


def print_genbank_record(gb_record): # print the gene bank record, such as id, starts sequence, end sequence and so on
    print('Found Sequence:', gb_record.id)
    print(gb_record.description)

    print('It starts:', gb_record.seq[:10])
    print('It ends:', gb_record.seq[-10:])
    print('It has %i nucleotides' % len(gb_record.seq))

    print('It has %i features.', len(gb_record.features))

    for feat in gb_record.features:
        print("Type:", feat.type)
        print("Location:", feat.location)


def find_orfs(seq): # creating a function for searching the orfs sequence based on the requirement.
    # set all initial condition
    start = 0
    forward_orf_count = 0
    orfs = []

    # asking the system to search the target sequence (both for reverse sequence and general sequence) which is starts at 'ATG'
    while start < len(seq):

        pos = seq.find('ATG', start)
        if pos == -1: #Found no more starts
            break

        start += pos

        forward_orf_count += 1
        orfs.append(seq[pos:].translate(to_stop = True))

    reverse_orf_count = 0
    start = 0
    nseq = seq.reverse_complement() #nseq is the reverse sequence

    while start < len(nseq):

        pos = nseq.find('ATG', start)
        if pos == -1: #Found no more starts
            break



        start += pos
        reverse_orf_count += 1
        # orfs.append(seq[pos:].translate(to_stop=True))
        orfs = seq_record[pos:].translate(to_stop=True)

    # print the result
    print('There are a total of %i forward ORFs and %i reverse ORFs' % (forward_orf_count, reverse_orf_count))
    return orfs

def main():

    # print_header()

    gb_path = get_genbank_path()

    with open(gb_path) as handle:
        for seq_record in SeqIO.parse(handle, 'genbank'):
            print_genbank_record(seq_record)
            seq_orfs = find_orfs(seq_record.seq)

            # saving all orf translate as a new handle in fasta style
            with open ('ORF_Translated.fasta', 'w') as handle:
                SeqIO.write(seq_orfs, handle, 'fasta')




if __name__ == '__main__':

    main()

