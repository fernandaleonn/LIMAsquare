def ortogonalidad_latina(cuadrado_1, cuadrado_2):
    for i in range(len(cuadrado_1)):
        for j in range(len(cuadrado_1)):
            for k in range(len(cuadrado_1)):
                for l in range(len(cuadrado_1)):
                    if (i, j) != (k, l):
                        if (cuadrado_1[k][l] == cuadrado_1[i][j] & cuadrado_2[k][l] == cuadrado_2[i][j]):
                           if(cuadrado_1[k][l] == cuadrado_2[i][j] and cuadrado_2[k][l] == cuadrado_1[i][j]):
                            return "No son ortogonales"


ortogonalidad_latina([[1,2,3],[3,2,1],[3,1,2]],[[1,2,3],[3,1,2],[2,3,1]])
