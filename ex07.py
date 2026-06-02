n1=int(input('digite a nota do primeiro bimestre:'))
n2=int(input('digite a nota do segundo bimestre:'))
n3=int(input("digite a nota do terceiro bimestre:"))
n4=int(input('digite a nota do quarto bimestre:'))
media=(n1+n2+n3+n4)/4
if media>=5:
    print(' sua media é {}, parabens você passou'.format(media))
else:
    print('sua media é {}, infelizmente você reprovou'.format(media))