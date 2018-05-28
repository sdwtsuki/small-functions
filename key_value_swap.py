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
            print(leval)
            for key in dict:
                print(key)
                for value in dict[key]:
                    print(value)
                    if leval == list(value)[0]:
                        value1, = value.values()
                        dict_swap[leval].append({key: value1})

        return dict_swap


dict2 = KeyValueSwap.key_value_swap1(dict1)
dict22 = KeyValueSwap.key_value_swap2(dict11)
print('这是原字典：'+str(dict11))
print('这是转换后的字典：'+str(dict22))