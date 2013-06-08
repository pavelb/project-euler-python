import unittest

class TestProjectEuler(unittest.TestCase):
	def test_001(self):
		module = __import__('001')
		answer = module.main(1000)
		self.assertEqual(answer, 233168)


	def test_002(self):
		module = __import__('002')
		answer = module.main(4000000)
		self.assertEqual(answer, 4613732)


	def test_003(self):
		module = __import__('003')
		answer = module.main(600851475143)
		self.assertEqual(answer, 6857)


	def test_004(self):
		module = __import__('004')
		answer = module.main(3)
		self.assertEqual(answer, 906609)


	def test_005(self):
		module = __import__('005')
		answer = module.main(20)
		self.assertEqual(answer, 232792560)


	def test_006(self):
		module = __import__('006')
		answer = module.main(100)
		self.assertEqual(answer, 25164150)


	def test_007(self):
		module = __import__('007')
		answer = module.main(10001)
		self.assertEqual(answer, 104743)


	def test_008(self):
		module = __import__('008')
		answer = module.main(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450, 5)
		self.assertEqual(answer, 40824)


	def test_009(self):
		module = __import__('009')
		answer = module.main(1000)
		self.assertEqual(answer, 31875000)


	def test_010(self):
		module = __import__('010')
		answer = module.main(2000000)
		self.assertEqual(answer, 142913828922)


	def test_011(self):
		module = __import__('011')
		answer = module.main([
			[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
			[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
			[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
			[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
			[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
			[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
			[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
			[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
			[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
			[21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
			[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
			[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
			[86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
			[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
			[4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
			[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
			[4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
			[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
			[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
			[1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
			], 4)
		self.assertEqual(answer, 70600674)


	def test_012(self):
		module = __import__('012')
		answer = module.main(500)
		self.assertEqual(answer, 76576500)


	def test_013(self):
		module = __import__('013')
		answer = module.main([
			37107287533902102798797998220837590246510135740250,
			46376937677490009712648124896970078050417018260538,
			74324986199524741059474233309513058123726617309629,
			91942213363574161572522430563301811072406154908250,
			23067588207539346171171980310421047513778063246676,
			89261670696623633820136378418383684178734361726757,
			28112879812849979408065481931592621691275889832738,
			44274228917432520321923589422876796487670272189318,
			47451445736001306439091167216856844588711603153276,
			70386486105843025439939619828917593665686757934951,
			62176457141856560629502157223196586755079324193331,
			64906352462741904929101432445813822663347944758178,
			92575867718337217661963751590579239728245598838407,
			58203565325359399008402633568948830189458628227828,
			80181199384826282014278194139940567587151170094390,
			35398664372827112653829987240784473053190104293586,
			86515506006295864861532075273371959191420517255829,
			71693888707715466499115593487603532921714970056938,
			54370070576826684624621495650076471787294438377604,
			53282654108756828443191190634694037855217779295145,
			36123272525000296071075082563815656710885258350721,
			45876576172410976447339110607218265236877223636045,
			17423706905851860660448207621209813287860733969412,
			81142660418086830619328460811191061556940512689692,
			51934325451728388641918047049293215058642563049483,
			62467221648435076201727918039944693004732956340691,
			15732444386908125794514089057706229429197107928209,
			55037687525678773091862540744969844508330393682126,
			18336384825330154686196124348767681297534375946515,
			80386287592878490201521685554828717201219257766954,
			78182833757993103614740356856449095527097864797581,
			16726320100436897842553539920931837441497806860984,
			48403098129077791799088218795327364475675590848030,
			87086987551392711854517078544161852424320693150332,
			59959406895756536782107074926966537676326235447210,
			69793950679652694742597709739166693763042633987085,
			41052684708299085211399427365734116182760315001271,
			65378607361501080857009149939512557028198746004375,
			35829035317434717326932123578154982629742552737307,
			94953759765105305946966067683156574377167401875275,
			88902802571733229619176668713819931811048770190271,
			25267680276078003013678680992525463401061632866526,
			36270218540497705585629946580636237993140746255962,
			24074486908231174977792365466257246923322810917141,
			91430288197103288597806669760892938638285025333403,
			34413065578016127815921815005561868836468420090470,
			23053081172816430487623791969842487255036638784583,
			11487696932154902810424020138335124462181441773470,
			63783299490636259666498587618221225225512486764533,
			67720186971698544312419572409913959008952310058822,
			95548255300263520781532296796249481641953868218774,
			76085327132285723110424803456124867697064507995236,
			37774242535411291684276865538926205024910326572967,
			23701913275725675285653248258265463092207058596522,
			29798860272258331913126375147341994889534765745501,
			18495701454879288984856827726077713721403798879715,
			38298203783031473527721580348144513491373226651381,
			34829543829199918180278916522431027392251122869539,
			40957953066405232632538044100059654939159879593635,
			29746152185502371307642255121183693803580388584903,
			41698116222072977186158236678424689157993532961922,
			62467957194401269043877107275048102390895523597457,
			23189706772547915061505504953922979530901129967519,
			86188088225875314529584099251203829009407770775672,
			11306739708304724483816533873502340845647058077308,
			82959174767140363198008187129011875491310547126581,
			97623331044818386269515456334926366572897563400500,
			42846280183517070527831839425882145521227251250327,
			55121603546981200581762165212827652751691296897789,
			32238195734329339946437501907836945765883352399886,
			75506164965184775180738168837861091527357929701337,
			62177842752192623401942399639168044983993173312731,
			32924185707147349566916674687634660915035914677504,
			99518671430235219628894890102423325116913619626622,
			73267460800591547471830798392868535206946944540724,
			76841822524674417161514036427982273348055556214818,
			97142617910342598647204516893989422179826088076852,
			87783646182799346313767754307809363333018982642090,
			10848802521674670883215120185883543223812876952786,
			71329612474782464538636993009049310363619763878039,
			62184073572399794223406235393808339651327408011116,
			66627891981488087797941876876144230030984490851411,
			60661826293682836764744779239180335110989069790714,
			85786944089552990653640447425576083659976645795096,
			66024396409905389607120198219976047599490197230297,
			64913982680032973156037120041377903785566085089252,
			16730939319872750275468906903707539413042652315011,
			94809377245048795150954100921645863754710598436791,
			78639167021187492431995700641917969777599028300699,
			15368713711936614952811305876380278410754449733078,
			40789923115535562561142322423255033685442488917353,
			44889911501440648020369068063960672322193204149535,
			41503128880339536053299340368006977710650566631954,
			81234880673210146739058568557934581403627822703280,
			82616570773948327592232845941706525094512325230608,
			22918802058777319719839450180888072429661980811197,
			77158542502016545090413245809786882778948721859617,
			72107838435069186155435662884062257473692284509516,
			20849603980134001723930671666823555245252804609722,
			53503534226472524250874054075591789781264330331690
		], 10)
		self.assertEqual(answer, 5537376230)


	def test_014(self):
		module = __import__('014')
		answer = module.main(1000000)
		self.assertEqual(answer, 837799)


	def test_015(self):
		module = __import__('015')
		answer = module.main(20, 20)
		self.assertEqual(answer, 137846528820)


	def test_015_0(self):
		module = __import__('015_0')
		answer = module.main(20, 20)
		self.assertEqual(answer, 137846528820)


	def test_015_1(self):
		module = __import__('015_1')
		answer = module.main(20, 20)
		self.assertEqual(answer, 137846528820)


	def test_016(self):
		module = __import__('016')
		answer = module.main(1000)
		self.assertEqual(answer, 1366)


	def test_017(self):
		module = __import__('017')
		answer = module.main(1000)
		self.assertEqual(answer, 21124)


	def test_018(self):
		module = __import__('018')
		answer = module.main('018.txt')
		self.assertEqual(answer, 1074)


	def test_019(self):
		module = __import__('019')
		answer = module.main()
		self.assertEqual(answer, 171)


	def test_020(self):
		module = __import__('020')
		answer = module.main(100)
		self.assertEqual(answer, 648)


	def test_021(self):
		module = __import__('021')
		answer = module.main(10000)
		self.assertEqual(answer, 31626)


	def test_022(self):
		module = __import__('022')
		answer = module.main('022.txt')
		self.assertEqual(answer, 871198282)


	def test_023(self):
		module = __import__('023')
		answer = module.main()
		self.assertEqual(answer, 4179871)


	def test_024(self):
		module = __import__('024')
		answer = module.main(range(10), 10 ** 6)
		self.assertEqual(answer, '2783915460')


	def test_025(self):
		module = __import__('025')
		answer = module.main(1000)
		self.assertEqual(answer, 4782)


	def test_026(self):
		module = __import__('026')
		answer = module.main(1000)
		self.assertEqual(answer, 983)

	def test_027(self):
		module = __import__('027')
		answer = module.main(1000, 1000)
		self.assertEqual(answer, -59231)


	def test_028(self):
		module = __import__('028')
		answer = module.main(1001)
		self.assertEqual(answer, 669171001)


	def test_029(self):
		module = __import__('029')
		answer = module.main(100, 100)
		self.assertEqual(answer, 9183)


	def test_030(self):
		module = __import__('030')
		answer = module.main(5)
		self.assertEqual(answer, 443839)


	def test_031(self):
		module = __import__('031')
		answer = module.main([1, 2, 5, 10, 20, 50, 100, 200], 200)
		self.assertEqual(answer, 73682)


	def test_031_0(self):
		module = __import__('031')
		answer = module.main([1, 2, 5, 10, 20, 50, 100, 200], 200)
		self.assertEqual(answer, 73682)


	def test_032(self):
		module = __import__('032')
		answer = module.main(9)
		self.assertEqual(answer, 45228)


	def test_033(self):
		module = __import__('033')
		answer = module.main()
		self.assertEqual(answer, 100)


	def test_034(self):
		module = __import__('034')
		answer = module.main()
		self.assertEqual(answer, 40730)


	def test_035(self):
		module = __import__('035')
		answer = module.main(1000000)
		self.assertEqual(answer, 55)


	def test_036(self):
		module = __import__('036')
		answer = module.main(1000000)
		self.assertEqual(answer, 872187)


	def test_037(self):
		module = __import__('037')
		answer = module.main(11)
		self.assertEqual(answer, 748317)


	def test_038(self):
		module = __import__('038')
		answer = module.main()
		self.assertEqual(answer, 932718654)


	def test_039(self):
		module = __import__('039')
		answer = module.main(1000)
		self.assertEqual(answer, 840)


	def test_040(self):
		module = __import__('040')
		answer = module.main([1, 10, 100, 1000, 10000, 100000, 1000000])
		self.assertEqual(answer, 210)


	def test_040_0(self):
		module = __import__('040_0')
		answer = module.main([1, 10, 100, 1000, 10000, 100000, 1000000])
		self.assertEqual(answer, 210)


	def test_040_1(self):
		module = __import__('040_1')
		answer = module.main([1, 10, 100, 1000, 10000, 100000, 1000000])
		self.assertEqual(answer, 210)


	def test_041(self):
		module = __import__('041')
		answer = module.main()
		self.assertEqual(answer, 7652413)


	def test_042(self):
		module = __import__('042')
		answer = module.main('042.txt')
		self.assertEqual(answer, 162)


	def test_043(self):
		module = __import__('043')
		answer = module.main()
		self.assertEqual(answer, 16695334890)


	def test_044(self):
		module = __import__('044')
		answer = module.main()
		self.assertEqual(answer, 5482660)


	def test_045(self):
		module = __import__('045')
		answer = module.main(40755)
		self.assertEqual(answer, 1533776805)


	def test_045_0(self):
		module = __import__('045_0')
		answer = module.main(40755)
		self.assertEqual(answer, 1533776805)


	def test_046(self):
		module = __import__('046')
		answer = module.main()
		self.assertEqual(answer, 5777)


	def test_047(self):
		module = __import__('047')
		answer = module.main(4, 4)
		self.assertEqual(answer, 134043)


	def test_048(self):
		module = __import__('048')
		answer = module.main(10, 1000)
		self.assertEqual(answer, 9110846700)


	def test_049(self):
		module = __import__('049')
		answer = module.main(4)
		self.assertEqual(answer, 296962999629)


	def test_050(self):
		module = __import__('050')
		answer = module.main(1000000)
		self.assertEqual(answer, 997651)


	def test_051(self):
		module = __import__('051')
		answer = module.main(8)
		self.assertEqual(answer, 121313)


	def test_052(self):
		module = __import__('052')
		answer = module.main(6)
		self.assertEqual(answer, 142857)


	def test_053(self):
		module = __import__('053')
		answer = module.main(100, 1000000)
		self.assertEqual(answer, 4075)


	def test_054(self):
		module = __import__('054')
		answer = module.main('054.txt')
		self.assertEqual(answer, 376)


	def test_055(self):
		module = __import__('055')
		answer = module.main(10000)
		self.assertEqual(answer, 249)


	def test_056(self):
		module = __import__('056')
		answer = module.main(100)
		self.assertEqual(answer, 972)


	def test_057(self):
		module = __import__('057')
		answer = module.main(1000)
		self.assertEqual(answer, 153)


	def test_058(self):
		module = __import__('058')
		answer = module.main(0.1)
		self.assertEqual(answer, 26241)


	def test_059(self):
		module = __import__('059')
		answer = module.main()
		self.assertEqual(answer, 107359)


	def test_060(self):
		module = __import__('060')
		answer = module.main(5)
		self.assertEqual(answer, 26033)


	def test_061(self):
		module = __import__('061')
		answer = module.main()
		self.assertEqual(answer, 28684)


	def test_062(self):
		module = __import__('062')
		answer = module.main(5)
		self.assertEqual(answer, 127035954683)


	def test_063(self):
		module = __import__('063')
		answer = module.main()
		self.assertEqual(answer, 49)


	def test_064(self):
		module = __import__('064')
		answer = module.main(10000)
		self.assertEqual(answer, 1322)


	def test_065(self):
		module = __import__('065')
		answer = module.main(100)
		self.assertEqual(answer, 272)


	def test_066(self):
		module = __import__('066')
		answer = module.main(1000)
		self.assertEqual(answer, 661)


	def test_067(self):
		module = __import__('067')
		answer = module.main('067.txt')
		self.assertEqual(answer, 7273)


	def test_068(self):
		module = __import__('068')
		answer = module.main(5, 16)
		self.assertEqual(answer, 6531031914842725)


	def test_069(self):
		module = __import__('069')
		answer = module.main(1000000)
		self.assertEqual(answer, 510510)


	def test_069_0(self):
		module = __import__('069_0')
		answer = module.main(1000000)
		self.assertEqual(answer, 510510)


	def test_070(self):
		module = __import__('070')
		answer = module.main(10 ** 7)
		self.assertEqual(answer, 8319823)


	def test_071(self):
		module = __import__('070')
		answer = module.main((3, 7), 1000000)
		self.assertEqual(answer, 428570)


	def test_072(self):
		module = __import__('072')
		answer = module.main(10 ** 6)
		self.assertEqual(answer, 303963552391)


	def test_073(self):
		module = __import__('073')
		answer = module.main((1, 3), (1, 2), 12000)
		self.assertEqual(answer, 7295372)


	def test_074(self):
		module = __import__('074')
		answer = module.main(10 ** 6)
		self.assertEqual(answer, 402)


	def test_075(self):
		module = __import__('075')
		answer = module.main(1500000)
		self.assertEqual(answer, 161667)


	def test_076(self):
		module = __import__('076')
		answer = module.main(100)
		self.assertEqual(answer, 190569291)


	def test_077(self):
		module = __import__('077')
		answer = module.main(5000)
		self.assertEqual(answer, 71)


	def test_078(self):
		module = __import__('078')
		answer = module.main(1000000)
		self.assertEqual(answer, 55374)


	def test_079(self):
		module = __import__('079')
		answer = module.main('079.txt')
		self.assertEqual(answer, 73162890)


	def test_080(self):
		module = __import__('080')
		answer = module.main()
		self.assertEqual(answer, 40886)


	def test_081(self):
		module = __import__('081')
		answer = module.main('081.txt')
		self.assertEqual(answer, 427337)


	def test_082(self):
		module = __import__('082')
		answer = module.main('082.txt')
		self.assertEqual(answer, 260324)


	def test_083(self):
		module = __import__('083')
		answer = module.main('083.txt')
		self.assertEqual(answer, 425185)


	def test_085(self):
		module = __import__('085')
		answer = module.main(2000000)
		self.assertEqual(answer, 2772)


	def test_086(self):
		module = __import__('086')
		answer = module.main(10 ** 6)
		self.assertEqual(answer, 1818)


	def test_086_0(self):
		module = __import__('086_0')
		answer = module.main(10 ** 6)
		self.assertEqual(answer, 1818)


	def test_087(self):
		module = __import__('087')
		answer = module.main(50000000)
		self.assertEqual(answer, 1097343)


	def test_088(self):
		module = __import__('088')
		answer = module.main(2, 12000)
		self.assertEqual(answer, 7587457)


	def test_089(self):
		module = __import__('089')
		answer = module.main("089.txt")
		self.assertEqual(answer, 743)


	def test_090(self):
		module = __import__('090')
		answer = module.main()
		self.assertEqual(answer, 1217)


	def test_091(self):
		module = __import__('091')
		answer = module.main(50)
		self.assertEqual(answer, 14234)


	def test_092(self):
		module = __import__('092')
		answer = module.main(10000000)
		self.assertEqual(answer, 8581146)


	def test_093(self):
		module = __import__('093')
		answer = module.main()
		self.assertEqual(answer, 1258)


	def test_094(self):
		module = __import__('094')
		answer = module.main(10 ** 9)
		self.assertEqual(answer, 518408346)


	def test_095(self):
		module = __import__('095')
		answer = module.main(1000000)
		self.assertEqual(answer, 14316)


	def test_096(self):
		module = __import__('096')
		answer = module.main('096.txt')
		self.assertEqual(answer, 24702)


	def test_097(self):
		module = __import__('097')
		answer = module.main(28433, 7830457, 10)
		self.assertEqual(answer, 8739992577)


	def test_098(self):
		module = __import__('098')
		answer = module.main('098.txt')
		self.assertEqual(answer, 18769)


	def test_099(self):
		module = __import__('099')
		answer = module.main('099.txt')
		self.assertEqual(answer, 709)


	def test_100(self):
		module = __import__('100')
		answer = module.main(10 ** 12)
		self.assertEqual(answer, 756872327473)


	def test_101(self):
		module = __import__('101')
		answer = module.main(10)
		self.assertEqual(answer, 37076114526)


	def test_102(self):
		module = __import__('102')
		answer = module.main('102.txt')
		self.assertEqual(answer, 228)


	def test_103(self):
		module = __import__('103')
		answer = module.main(7)
		self.assertEqual(answer, 20313839404245)


	def test_104(self):
		module = __import__('104')
		answer = module.main()
		self.assertEqual(answer, 329468)


	def test_105(self):
		module = __import__('105')
		answer = module.main('105.txt')
		self.assertEqual(answer, 73702)


	def test_106(self):
		module = __import__('106')
		answer = module.main(12)
		self.assertEqual(answer, 21384)


	def test_107(self):
		module = __import__('107')
		answer = module.main('107.txt')
		self.assertEqual(answer, 259679)


	def test_108(self):
		module = __import__('108')
		answer = module.main(1000)
		self.assertEqual(answer, 180180)


	def test_110(self):
		module = __import__('110')
		answer = module.main(4000000)
		self.assertEqual(answer, 9350130049860600)


	def test_111(self):
		module = __import__('111')
		answer = module.main(10)
		self.assertEqual(answer, 612407567715)


	def test_112(self):
		module = __import__('112')
		answer = module.main(0.99)
		self.assertEqual(answer, 1587000)


	def test_113(self):
		module = __import__('113')
		answer = module.main(100)
		self.assertEqual(answer, 51161058134250)


	def test_114(self):
		module = __import__('114')
		answer = module.main(3, 50)
		self.assertEqual(answer, 16475640049)


	def test_115(self):
		module = __import__('115')
		answer = module.main(50, 1000000)
		self.assertEqual(answer, 168)


	def test_116(self):
		module = __import__('116')
		answer = module.main(50, 4)
		self.assertEqual(answer, 20492570929)


	def test_117(self):
		module = __import__('117')
		answer = module.main(4, 50)
		self.assertEqual(answer, 100808458960497)


	def test_117_0(self):
		module = __import__('117_0')
		answer = module.main(4, 50)
		self.assertEqual(answer, 100808458960497)


	def test_118(self):
		module = __import__('118')
		answer = module.main([1, 2, 3, 4, 5, 6, 7, 8, 9])
		self.assertEqual(answer, 44680)


	def test_118_0(self):
		module = __import__('118_0')
		answer = module.main([1, 2, 3, 4, 5, 6, 7, 8, 9])
		self.assertEqual(answer, 44680)


	def test_119(self):
		module = __import__('119')
		answer = module.main(30)
		self.assertEqual(answer, 248155780267521)


	def test_120(self):
		module = __import__('120')
		answer = module.main(3, 1000)
		self.assertEqual(answer, 333082500)


	def test_121(self):
		module = __import__('121')
		answer = module.main(15)
		self.assertEqual(answer, 2269)


	def test_123(self):
		module = __import__('123')
		answer = module.main(10 ** 10)
		self.assertEqual(answer, 21035)


	def test_124(self):
		module = __import__('124')
		answer = module.main(100000, 10000)
		self.assertEqual(answer, 21417)


	def test_129(self):
		module = __import__('129')
		answer = module.main(10 ** 6)
		self.assertEqual(answer, 1000023)


	def test_131(self):
		module = __import__('131')
		answer = module.main(10 ** 6)
		self.assertEqual(answer, 173)


	def test_132(self):
		module = __import__('132')
		answer = module.main(10 ** 9, 40)
		self.assertEqual(answer, 843296)


	def test_134(self):
		module = __import__('134')
		answer = module.main()
		self.assertEqual(answer, 18613426663617118)


	def test_135(self):
		module = __import__('135')
		answer = module.main(1000000, 10)
		self.assertEqual(answer, 4989)


	def test_136(self):
		module = __import__('136')
		answer = module.main(50000000, 1)
		self.assertEqual(answer, 2544559)


	def test_137(self):
		module = __import__('137')
		answer = module.main(15)
		self.assertEqual(answer, 1120149658760)


	def test_138(self):
		module = __import__('138')
		answer = module.main(12)
		self.assertEqual(answer, 1118049290473932)


	def test_162(self):
		module = __import__('162')
		answer = module.main(16)
		self.assertEqual(answer, '3D58725572C62302')


	def test_164(self):
		module = __import__('164')
		answer = module.main(20)
		self.assertEqual(answer, 378158756814587)


	def test_169(self):
		module = __import__('169')
		answer = module.main(10 ** 25 + 1)
		self.assertEqual(answer, 178653872807)


	def test_173(self):
		module = __import__('173')
		answer = module.main(10 ** 6)
		self.assertEqual(answer, 1572729)


	def test_174(self):
		module = __import__('174')
		answer = module.main()
		self.assertEqual(answer, 209566)


	def test_183(self):
		module = __import__('183')
		answer = module.main(10 ** 4)
		self.assertEqual(answer, 48861552)


	def test_187(self):
		module = __import__('187')
		answer = module.main(10 ** 8)
		self.assertEqual(answer, 17427258)


	def test_188(self):
		module = __import__('188')
		answer = module.main(8, 1777, 1855)
		self.assertEqual(answer, 95962097)


	def test_191(self):
		module = __import__('191')
		answer = module.main(30)
		self.assertEqual(answer, 1918080160)


	def test_197(self):
		module = __import__('197')
		answer = module.main()
		self.assertEqual(answer, 1.710637717)


	def test_203(self):
		module = __import__('203')
		answer = module.main(51)
		self.assertEqual(answer, 34029210557338)


	def test_204(self):
		module = __import__('204')
		answer = module.main(100, 10 ** 9)
		self.assertEqual(answer, 2944730)


	def test_205(self):
		module = __import__('205')
		answer = module.main(4, 9, 6, 6)
		self.assertEqual(answer, 0.5731441)


	def test_206(self):
		module = __import__('206')
		answer = module.main()
		self.assertEqual(answer, 1389019170)


	def test_207(self):
		module = __import__('207')
		answer = module.main(1.0 / 12345)
		self.assertEqual(answer, 44043947822)


	def test_214(self):
		module = __import__('214')
		answer = module.main(40000000, 25)
		self.assertEqual(answer, 1677366278943)


	def test_214_0(self):
		module = __import__('214_0')
		answer = module.main(40000000, 25)
		self.assertEqual(answer, 1677366278943)


	def test_225(self):
		module = __import__('225')
		answer = module.main(124)
		self.assertEqual(answer, 2009)


	def test_235(self):
		module = __import__('235')
		answer = module.main()
		self.assertEqual(answer, 1.002322108633)


	def test_243(self):
		module = __import__('243')
		answer = module.main(15499, 94744)
		self.assertEqual(answer, 892371480)


if __name__ == '__main__':
    unittest.main()
