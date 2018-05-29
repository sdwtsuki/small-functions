import xlwt
#字典键值对换
dict1 = {}
dict1['/iː/'] = ['ee','ea','e','ie','ei']
dict1['/ɪ/'] = ['i','y','e','ui','u','a']
dict1['/æ/'] = ['a']
dict1['/e/'] = ['e','a','ea']
dict1['/ɜː/'] = ['or','ir','er','ur','ear']
dict1['/ə/'] = ['a','er','or','o','ure','ur','e','iou','ou','ar']
dict1['/ʌ/'] = ['u','o','ou','oo']


dict11 = {}
dict11['/iː/'] = [{'ee':'beef'},{'ea':'meat'},{'e':'me'},{'ie':'achieve'},{'ei':'deceive'}]
dict11['/ɪ/'] = [{'i':'sit'},{'y':'many'},{'e':'pretty'},{'ui':'quick'},{'u':'business'},{'a':'private'}]

dict11['/æ/'] = [{'a':'apple'}]
dict11['/e/'] = [{'e':'pen'},{'a':'many'},{'ea':'bread'}]
dict11['/ɜː/'] = [{'or':'work'},{'ir':'girl'},{'er':'person'},{'ur':'turn'},{'ear':'early'}]
dict11['/ə/'] = [{'a':'away'},{'er':'teacher'},{'or':'doctor'},{'o':'together'},{'ure':'picture'},{'ur':'saturday'},{'e':'open'},{'iou':'delicious'},{'ou':'colour'},{'ar':'dollar'}]
dict11['/ʌ/'] = [{'u':'luck'},{'o':'onion'},{'ou':'trouble'},{'oo':'blood'}]

dict11['/uː/'] = [{'oo':'school'},{'o':'woman'},{'ou':'soup'},{'u':'rule'},{'oe':'shoe'},{'ui':'juice'},{'ew':'jewel'}]
dict11['/ʊ/'] = [{'oo':'foot'},{'u':'pull'},{'ou':'should'}]
dict11['/ɔː/'] = [{'ai':'talk'},{'oo':'door'},{'aw':'law'},{'ou':'bought'},{'ore':'ignore'},{'au':'caught'},{'or':'force'},{'oar':'soar'}]
dict11['/ɒ/'] = [{'o':'hot'},{'a':'wash'}]
dict11['/ɑː/'] = [{'a':'class'},{'ar':'arm'},{'ear':'hear'},{'al':'calm'}]

dict11['/eɪ/'] = [{'ei':'weight'},{'a':'famous'},{'ai':'main'},{'ay':'day'}]
dict11['/aɪ/'] = [{'y':'cry'},{'i':'kite'},{'uy':'buy'}]
dict11['/ɔɪ/'] = [{'oy':'toy'},{'oi':'voice'}]
dict11['/aʊ/'] = [{'ou':'sound'},{'ow':'town'}]
dict11['/əʊ/'] = [{'o':'host'},{'ow':'bowl'},{'oa':'boat'},{'oe':'woe'}]

dict11['/ɪə/'] = [{'eer':'beer'},{'ear':'hear'},{'ere':'sincere'},{'ea':'area'}]
dict11['/eə/'] = [{'air':'hair'},{'ear':'bear'},{'are':'dare'},{'ere':'there'}]
dict11['/ʊə/'] = [{'oor':'poor'},{'ure':'ensure'},{'our':'tour'}]

dict11['/p/'] = [{'p':'pay'},{'pp':'happen'}]
dict11['/t/'] = [{'t':'teacher'},{'tt':'little'},{'ed':'watched'}]
dict11['/k/'] = [{'c':'cake'},{'k':'keep'},{'ck':'pick'},{'ch':'school'}]

dict11['/b/'] = [{'b':'bake'},{'bb':'rubbish'}]
dict11['/d/'] = [{'d':'bed'},{'dd':'middle'}]
dict11['/ɡ/'] = [{'g':'geese'},{'gg':'luggage'}]

dict11['/f/'] = [{'f':'five'},{'ph':'telephone'},{'ff':'office'},{'gh':'laugh'}]
dict11['/s/'] = [{'s':'mouse'},{'ss':'mass'},{'c':'face'},{'sc':'scent'}]
dict11['/ʃ/'] = [{'sh':'ship'},{'s':'sure'},{'ss':'assure'},{'ch':'machine'},{'ci':'social'},{'ti':'station'}]
dict11['/θ/'] = [{'th':'breath'}]
dict11['/h/'] = [{'h':'hot'},{'wh':'who'}]

dict11['/v/'] = [{'v':'vote'}]
dict11['/z/'] = [{'z':'zoo'},{'s':'raise'},{'zz':'puzzle'},{'x':'xerox'}]
dict11['/ʒ/'] = [{'su':'pleasure'},{'si':'collision'},{'ge':'garage'}]
dict11['/ð/'] = [{'th':'though'}]
dict11['/r/'] = [{'r':'rise'},{'rr':'arrive'},{'wr':'write'}]

dict11['/tʃ/'] = [{'ch':'chain'},{'t':'future'},{'tch':'catch'}]
dict11['/tr/'] = [{'tr':'tree'}]
dict11['/ts/'] = [{'ts':'parents'}]

dict11['/dʒ/'] = [{'g':'large'},{'dge':'judge'},{'j':'just'},{'du':'schedule'}]
dict11['/dr/'] = [{'dr':'dream'}]
dict11['/dz/'] = [{'ds':'needs'}]

dict11['/m/'] = [{'m':'some'},{'mm':'common'}]
dict11['/n/'] = [{'n':'nose'},{'nn':'dinner'},{'gn':'sign'}]
dict11['/ŋ/'] = [{'ng':'long'},{'n':'anger'}]

dict11['/l/'] = [{'l':'laid'}]

dict11['/j/'] = [{'y':'young'},{'i':'million'}]
dict11['/w/'] = [{'i':'sit'}]



class KeyValueSwap:
    def key_value_swap1(dict):
        letter1 = []
        for each in dict:
            list1 = dict[each]
            for le in list1:
                letter1.append(le)

        letter2 = list(set(letter1))
        dict_swap = {}

        for leval in letter2:
            dict_swap[leval] = []
            for key in dict:
                for value in dict[key]:
                    if leval == value:
                        dict_swap[leval].append(key)

        return dict_swap


    def key_value_swap2(dict):
        letter1 = []
        for each in dict:
            list1 = dict[each]
            for le in list1:
                le1, = le
                letter1.append(le1)

        letter2 = list(set(letter1))
        dict_swap = {}

        for leval in letter2:
            dict_swap[leval] = []
            for key in dict:
                for value in dict[key]:
                    if leval == list(value)[0]:
                        value1, = value.values()
                        dict_swap[leval].append({key: value1})

        return dict_swap


dict2 = KeyValueSwap.key_value_swap1(dict1)
dict22 = KeyValueSwap.key_value_swap2(dict11)
print('这是原字典：'+str(dict11))
print('这是转换后的字典：'+str(dict22))

book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('Sheet1')

i = 0
for key in dict22:
    i += 1
    for j in range(0,len(dict22[key])):
        phonetic, = dict22[key][j]
        example, = dict22[key][j].values()
        if j==0:
            sheet.write(i, 0, key)
        sheet.write(i, j*2+1, phonetic)
        sheet.write(i, j*2+2, example)


book.save('yinbiao.xls')
