import time
import math
p=2999110324470563466830036499463565800214205396087477484933603866965624339163441164953138336136852538549885533678016598576591328844071561139769180701327735263911826386554138383665464461182791877365370914522657262727410659574991513
q=7517067481852007491722406907553383657302210090194854290590288541705759006664552789857005296232434117422268750306067947012230019560159259832855661617633661176428234674468364245171998780892019921485661482260757652780517722153903591734250483
n=22544514694564295643205628221802970349068543924599967262171703694675036988567412502970706346591056487289694229846284871148871382847513168616415053473259889998875830940694251351604661323561573844661356151999154073365470946228865048952800073907294373461402795276582583778270425195656508980282384181767166336827087588072252529030797739898797001790934844245821445163188470135456712602498784774822857865884438244715430846508115098293810878189104137422287777509276141150779
m=22544514694564295643205628221802970349068543924599967262171703694675036988567412502970706346591056487289694229846284871148871382847513168616415053473259889998875830940694251351604661323561573844661356151999154073365470946228865041435732589056176557268432420893162427012494534786596822302516357542404292706649958567625791343458344180777508145837454153999203308412599793208233955199656907018852919485693806518578266289023732429840451252060536834247302896195024831908784
e=237006802130181
d=78305184667957370580898543732507983176916395591161516437945441982103878016573543735187340355971391080588258864150790630216692512706937437848170514233586267162774935872144489863151901726158730763677526430155790846179405650476042745591064917192845262455520373046456457889958156863540494785223468561284559602435846229611892963818735083504018211278600636572002681918516880907065761518476410338029015006856032392412716830140644612256091582776209469164348513578686237467709
a=10671640584264483651281659067099072129710763817361614651430330898078767050871306226275221316198221618719176174611936016770078364164397931998925353813806597166147443050061735808337917755474009229693457974158328626082992811789447621283867150024315590650223110366969176852474552503750027877674395934071681482485970526734518933443702541171493773766238174574392756680717501282363895919505689281470256549774612836677917963069447322734737826594598966422439824993611741741357
k=3
B=pow(2, 1, n)

temp = time.time()
for i in range((n-2*int(n**0.5)+1//4)*4,n,4):
    if i%10000==0:
        print(i)
        print(time.time()-temp)
        temp = time.time()
    if pow(2,1+i,n)==B:
        print(i)