test_dict = {}
test_in_dict = {'주소': 'https://naver.com', '인원': '100명', '주소': '서울특별시'}

key_names = ['a', 'b', 'c']
value_params = ['유환국', '가나다', '사람', '어쩌고 저쩌고']

for key_name in key_names:
    test_dict[key_name] = test_in_dict


len(test_dict)
a = test_dict.keys()
test_dict
type(a)


dict(zip(company_keys, url_vals))


a_keys = ['a_1', 'a_2', 'a_3']
a_vals = [1, 2, 3]

b_keys = ['b_1', 'b_2', 'b_3']
b_vals = [10, 20, 30]

test_dict = dict(zip(a_keys, a_vals))
test_dict = dict(zip(b_keys, b_vals))
