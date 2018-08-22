from lingpy import *
from lingpy.evaluate.acd import bcubes
from lingpy.convert.tree import *
from lingpy.convert.plot import plot_heatmap

def make_matrix(ref, wordlist, tree, tree_taxa):
    
    matrix = [[1 for i in tree_taxa] for j in tree_taxa]
    for i, tA in enumerate(tree_taxa):
        for j, tB in enumerate(tree_taxa):
            if i < j:
                cogsA = wordlist.get_dict(col=tA, entry=ref)
                cogsB = wordlist.get_dict(col=tB, entry=ref)
                shared, slots = 0, 0
                for key in set([k for k in cogsA] + [k for k in cogsB]):
                    if key in cogsB and key in cogsA:
                        if [c for c in cogsA[key] if c in cogsB[key]]:
                            shared += 1
                        slots += 1

                matrix[i][j] = shared / slots
                matrix[j][i] = shared / slots
    return matrix

def load_matrix(fname):
    data = csv2list(fname)
    taxa = [line[0].strip() for line in data]
    matrix = [[0 for i in taxa] for j in taxa]
    for i in range(len(taxa)):
        for j in range(1, len(taxa)+1):
            matrix[i][j-1] = float(data[i][j])
    return taxa, matrix


#tree = "((Bambara,Jenaama),Bangime,(('Toro_Tegu',((('Tebul_Ure','Yanda_Dom'),(('Tommo_So','Yorno_So'),('Togo_Kan',(Jamsay,'Perge_Tegu')))),(Nanga,('Bankan_Tey','Ben_Tey')))),((Bunoge,(Mombo,Penange)),(Najamba,'Tiranige_Diga'))),Fulfulde,('Songhai_Kiini','Songhai_Senni'));"
#tm, tree_taxa = nwk2tree_matrix(tree)


for i in [100, 200, 300]:
    try:
        lex = LexStat('D_subset-{0}-22.tsv.bin.tsv'.format(i))
    except:
        lex = LexStat('D_subset-{0}-22.tsv'.format(i))
        lex.get_scorer(runs=10000, restricted_chars='_')
        lex.output('tsv', filename=lex.filename+'.bin', ignore='')
    lex.cluster(method='sca', threshold=0.45, ref='scaid', restricted_chars='_')
    lex.cluster(method='lexstat', threshold=0.55, restricted_chars='_',
            ref='lexstatid', cluster_method='infomap')
    p, r, f = bcubes(lex, 'lexstatid', 'scaid', pprint=False)
    print('SuSe{0} {1:.2f} {2:.2f} {3:.2f}'.format(i, p, r, f))

    lex.output('tsv', filename=lex.filename+'-cognates', ignore='all')
    lex.calculate('tree', ref='lexstatid')
    
    tm, tree_taxa = nwk2tree_matrix(lex.tree)
    matrix1 = make_matrix('lexstatid', lex, lex.tree, tree_taxa)
    matrix2 = make_matrix('scaid', lex, lex.tree, tree_taxa)


    plot_heatmap(lex, ref='lexstatid', filename='O_lexstat_{0}'.format(i), vmax=1,
            tree=lex.tree, colorbar_label='lexical cognates',
            normalized='swadesh',
            )
    plot_heatmap(lex, ref='scaid', filename='O_sca_{0}'.format(i), vmax=1,
            tree=lex.tree, colorbar_label='lexical cognates',
            normalized='swadesh')

    _, matrix1 = load_matrix('O_lexstat_{0}.matrix'.format(i))
    _, matrix2 = load_matrix('O_sca_{0}.matrix'.format(i))

    new_matrix = [[0 for x in range(len(matrix1[0]))] for y in
            range(len(matrix1))]
    for _i in range(len(matrix1)):
        for _j in range(len(matrix1)):
            new_matrix[_i][_j] = 0.5 + (matrix2[_i][_j] - matrix1[_i][_j])
    plot_heatmap(lex, ref='lexstatid', matrix=new_matrix, tree=lex.tree,
            colorbar_label='differences (inferred cognates)', filename='O_combined_{0}'.format(i),
            vmax=0.7, vmin=0.3)
    



    






