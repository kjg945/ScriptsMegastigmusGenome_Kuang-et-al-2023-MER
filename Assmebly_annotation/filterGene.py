##Only the genes with the specified ID in the fasta file are retained

Filter the gene with the specified ID in the fasta file

with open('MD_id.txt', 'r') as f:
    data = f.read().split('\n')
print(data)
with open('MD_pep.fasta', 'r') as g:
    fasta = g.read().split('\n')
    
for index, i in enumerate(fasta):
    if i.startswith('>'):
        _id = i[1:]
        if _id in data:
            newID = '>' + _id + '\n'
            f = fasta[index + 1] + '\n'
            with open('new.fasta', 'a+') as file:
                file.write(newID)
                file.write(f)