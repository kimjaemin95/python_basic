'''
외부 설치 패키지 테스트
'''

import simplejson as json

jm_dict = { 'Kim':95, 'Lee':32, 'Choi':12, 'Boo':84 }

# simplejson 실행
print(json.dumps(jm_dict, sort_keys=True, indent=4 * ' '))






