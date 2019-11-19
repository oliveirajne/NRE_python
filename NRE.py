

#variaveis

N, i = 0, 0

f_1, f_2, df_1dx, df_1dy, df_2dx, df_2dy, x, y, e, x_0 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
y_0, d_1, x_i, y_i, x_im1, y_im1, VAf_1, VAf_2, VAf_max, VAS_1 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
VAS_2, VAS_max, VAX, VAY, VAXY = 0, 0, 0, 0, 0
J = [2,2]
F, S = [0,0], [0,0]

#atribuicoes

x_0 = 1.0e00 
y_0 = 2.0e00 
e = 1.0e-6
N = 10
x_i = x_0
y_i = y_0

#funcoes

def funcao_1(x,y):
	fx = x + y - 3.0e0
	return fx
	
def funcao_2(x,y):
	fx = x**2 + y**2 - 9.0e0
	return fx
	
def derivada_1dx(x,y):
	fx = 1.0e0
	return fx

def derivada_1dy(x,y):
	fx = 1.0e0
	return fx
	
def derivada_2dx(x,y):
	fx = 2.0e0*x
	return fx

def derivada_2dy(x,y):
	fx = 2.0e0*y
	return fx
	
def TRI(A, M):
    FAC = 0
    A = A
    TOLPIV = 1.e-11
    M1     = M-1

	
    for i in range(0, M):
        if ( abs(A[i][i]) < TOLPIV ):
            print("Pivo muito pequeno.")
            break
        
        J1 = i + 1
        
        for j in range(J1, M):

            FAC = A[i][j]/A[i][i]

            for k in range(J1, M):

                A[j][k] = A[j][k] - A[k][i] * FAC

    return 
	
def RHSUB(A, B, M, S):

    M1 = M-1



    for i in range(0, M):
        J1  = i + 1
        
        for j in range(J1, M):

            B[j] = B[j] - B[i]*A[j][i]/A[i][i]

            S[M-1] = B[M-1]/A[M-1][M-1]

    for i in range(0, M):
        IB = M - 1
        J1 = i + 1 
        
        for j in range(J1, M):

            B[IB-1] = B[IB-1] - A[IB-1][j-1]*S[j]


        S[IB-1] = B[IB-1]/A[IB-1][IB-1]

    return

for i in range(0, N+1):

    print(x_im1)
    print(VAf_max)
   
    J = [[derivada_1dx(x_i,y_i),derivada_2dx(x_i,y_i)], [derivada_1dy(x_i,y_i),derivada_2dy(x_i,y_i)]] 
	
    F = [-funcao_1(x_i,y_i),-funcao_2(x_i,y_i)]

    TRI(J, 2)
    RHSUB(J, F, 2, S)

    x_im1 = S[0] + x_i
    print("x_im1 " + "{0:16e}".format(x_im1))
    print("S[0] " + "{0:16e}".format(S[0]))
    print("x_i "+"{0:16e}".format(x_i))
    y_im1 = S[1] + y_i

    VAf_1 = abs(funcao_1(x_im1,y_im1))

    VAf_2 = abs(funcao_2(x_im1,y_im1))

    print(S)
    print('aha')
    print(x_im1)
    print(y_im1)
    if ( VAf_1 < VAf_2):
        VAf_max = VAf_2
    else:        
        VAf_max = VAf_1
        print('MANOOOOOOOOOOOOOOOO')
        print(VAf_1)
        print(VAf_2)
        
    VAS_1 = abs(S[0])
    VAS_2 = abs(S[1])
    
    if ( VAS_1 < VAS_2):
        VAS_max = VAS_2
    else:
        VAS_max = VAS_1
        
    VAX = x_im1
    VAY = y_im1

    if ( VAX < VAY):
        VAXY = VAY
    else:
        VAXY = VAX

    d_1= VAS_max 

    
    if (VAXY != 0.0e0): 
        d_1=d_1/VAXY
        if (d_1 <= e):
            if (VAf_max <= e):
                
                print("{0:5}".format(i), "{0:16e}".format(x_im1), "{0:16e}".format(y_im1), "{0:16e}".format(VAf_max), "{0:16e}".format(d_1))   
                break
 
    x_i = x_im1 
    y_i = y_im1 

    print("{0:5}".format(i), "{0:16e}".format(x_im1), "{0:16e}".format(y_im1), "{0:16e}".format(VAf_max), "{0:16e}".format(d_1))
    # print(i, x_im1, y_im1, VAf_max, d_1)
