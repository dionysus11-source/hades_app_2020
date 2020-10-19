#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json

def makeHadesData():
    data = []
    zeus_poseidon = {}
    zeus_poseidon['name'] = '바다 폭풍'
    zeus_poseidon['condition'] =[['공격', '특공', '전기마법', '천둥마법' ,'돌진', '지원'], ['공격', '특공', '마법', '돌진', '지원']]
    zeus_poseidon['owner'] = {'제우스' : 0, '포세이돈' : 1}
    zeus_poseidon['description'] = '적을 밀치면 적에게 벼락이 떨어집니다.'
    zeus_poseidon['is_selected'] = [False, False]
    data.append(zeus_poseidon)

    zeus_athena = {}
    zeus_athena['name'] = '벼락 방진'
    zeus_athena['condition'] =[['공격', '특공', '천둥마법' ,'돌진', '지원'], ['탄환마법']]
    zeus_athena['owner'] = {'제우스' : 0, '아테나' : 1}
    zeus_athena['description'] = '벼락 방진 마법은 인근의 적들 사이에서 튕기며 타격합니다.'
    zeus_athena['is_selected'] = [False, False]
    data.append(zeus_athena)

    zeus_apro = {}
    zeus_apro['name'] = '그을린 공기'
    zeus_apro['condition'] =[['공격', '특공', '전기마법' ,'천둥마법','돌진', '지원'], ['공격', '특공', '마법', '돌진', '지원']]
    zeus_apro['owner'] = {'제우스' : 0, '아프로디테' : 1}
    zeus_apro['description'] = '신 게이지가 자동으로 충전되지만 25%이상 오르지 않습니다.'
    zeus_apro['is_selected'] = [False, False]
    data.append(zeus_apro)

    zeus_artemis = {}
    zeus_artemis['name'] = '피뢰침'
    zeus_artemis['condition'] =[['공격', '특공', '전기마법' ,'천둥마법' ,'돌진', '지원'], ['공격', '특공', '탄환마법2','섬광마법2' '돌진', '지원']]
    zeus_artemis['owner'] = {'제우스' : 0, '아르테미스' : 1}
    zeus_artemis['description'] = '매 1초마다 혈석을 회수할 때 인근의 적들에게 벼락을 내립니다.'
    zeus_artemis['is_selected'] = [False, False]
    data.append(zeus_artemis)

    zeus_ares = {}
    zeus_ares['name'] = '복수심에 불타는 기분'
    zeus_ares['condition'] =[['공격', '특공', '전기마법' ,'천둥마법' ,'돌진', '지원','반격'], ['공격', '특공', '탄환마법2','섬광마법2', '돌진', '지원','반격']]
    zeus_ares['owner'] = {'제우스' : 0, '아레스' : 1}
    zeus_ares['description'] = '복수 효과는 때때로 피해를 입지 않고도 발생합니다.'
    zeus_ares['is_selected'] = [False, False]
    data.append(zeus_ares)

    zeus_dionysus = {}
    zeus_dionysus['name'] = '반짝이는 축제'
    zeus_dionysus['condition'] =[['공격', '특공', '전기마법' ,'천둥마법' ,'돌진', '지원'], ['마법','마법강화']]
    zeus_dionysus['owner'] = {'제우스' : 0, '디오니소스' : 1}
    zeus_dionysus['description'] = '축제 안개는 주기적으로 벼락도 내립니다.'
    zeus_dionysus['is_selected'] = [False, False]
    data.append(zeus_dionysus)

    poseidon_athena = {}
    poseidon_athena['name'] = '요지부동 기개'
    poseidon_athena['condition'] =[['공격', '특공', '마법' ,'돌진', '지원'], ['공격', '특공', '탄환마법','섬광마법', '돌진', '지원']]
    poseidon_athena['owner'] = {'포세이돈' : 0, '아테나' : 1}
    poseidon_athena['description'] = '적의 공격에 더 이상 기절하지 않고 보스에게서 입는 피해가 감소합니다.'
    poseidon_athena['is_selected'] = [False, False]
    data.append(poseidon_athena)

    poseidon_apro = {}
    poseidon_apro['name'] = '달콤한 넥타르'
    poseidon_apro['condition'] =[['공격', '특공', '마법' ,'돌진', '지원'], ['공격', '특공', '마법', '돌진', '지원']]
    poseidon_apro['owner'] = {'포세이돈' : 0, '아프로디테' : 1}
    poseidon_apro['description'] = '얻는 모든 힘의 석류가 더 좋아집니다.'
    poseidon_apro['is_selected'] = [False, False]
    data.append(poseidon_apro)

    poseidon_artemis = {}
    poseidon_artemis['name'] = '신기루 사격'
    poseidon_artemis['condition'] =[['공격', '특공', '마법' ,'돌진', '지원'], ['공격', '특공', '마법', '돌진', '지원']]
    poseidon_artemis['owner'] = {'포세이돈' : 0, '아르테미스' : 1}
    poseidon_artemis['description'] = '마법은 기본 피해량이 더 적은 보조 발사체를 발사합니다.'
    poseidon_artemis['is_selected'] = [False, False]
    data.append(poseidon_artemis)

    poseidon_ares = {}
    poseidon_ares['name'] = '악사의 저주'
    poseidon_ares['condition'] =[['마법'], ['공격', '특공', '돌진', '지원']]
    poseidon_ares['owner'] = {'포세이돈' : 0, '아레스' : 1}
    poseidon_ares['description'] = '홍수 탄환이 주변 적에게 피해를 가하는 파동이 됩니다.'
    poseidon_ares['is_selected'] = [False, False]
    data.append(poseidon_ares)

    poseidon_dionysus = {}
    poseidon_dionysus['name'] = '특권'
    poseidon_dionysus['condition'] =[['공격', '특공', '마법' ,'돌진', '지원'], ['공격', '특공', '마법', '돌진', '지원']]
    poseidon_dionysus['owner'] = {'포세이돈' : 0, '디오니소스' : 1}
    poseidon_dionysus['description'] = '얻는 모든 은혜가 더 좋아집니다.'
    poseidon_dionysus['is_selected'] = [False, False]
    data.append(poseidon_dionysus)

    zeus_deme = {}
    zeus_deme['name'] = '저온융합'
    zeus_deme['condition'] =[['피해강화'], ['공격', '특공','돌진', '지원']]
    zeus_deme['owner'] = {'제우스' : 0, '데메테르' : 1}
    zeus_deme['description'] = '충격 효과는 적이 공격을 해도 사라지지 않습니다.'
    zeus_deme['is_selected'] = [False, False]
    data.append(zeus_deme)

    poseidon_deme = {}
    poseidon_deme['name'] = '눈보라탄환'
    poseidon_deme['condition'] =[['마법'], ['공격', '특공', '돌진', '지원']]
    poseidon_deme['owner'] = {'포세이돈' : 0, '데메테르' : 1}
    poseidon_deme['description'] = '마법은 느리게 날아가며 적들을 관통하고 파편을 날립니다.'
    poseidon_deme['is_selected'] = [False, False]
    data.append(poseidon_deme)

    athena_apro = {}
    athena_apro['name'] = '갈라진 사격'
    athena_apro['condition'] =[['공격', '특공', '탄환마법','섬광마법' ,'돌진', '지원'], ['공격', '특공', '마법', '돌진', '지원']]
    athena_apro['owner'] = {'아테나' : 0, '아프로디테' : 1}
    athena_apro['description'] = '마법은 배후 공격의 추가효과 또한 얻습니다.'
    athena_apro['is_selected'] = [False, False]
    data.append(athena_apro)

    athena_artemis = {}
    athena_artemis['name'] = '치명적인 반격'
    athena_artemis['condition'] =[['공격', '특공'], ['공격', '특공', '탄환마법2', '섬광마법2', '지원']]
    athena_artemis['owner'] = {'아테나' : 0, '아르테미스' : 1}
    athena_artemis['description'] = '반사 후 잠시 동안 +20% 확률로 치명타를 가합니다.'
    athena_artemis['is_selected'] = [False, False]
    data.append(athena_artemis)

    athena_ares = {}
    athena_ares['name'] = '자비로운 최후'
    athena_ares['condition'] =[['공격', '특공'], ['공격', '특공']]
    athena_ares['owner'] = {'아테나' : 0, '아레스' : 1}
    athena_ares['description'] = '반사할 수 있는 능력은 파멸 효과를 즉시 발동시킵니다.'
    athena_ares['is_selected'] = [False, False]
    data.append(athena_ares)

    athena_dionysus = {}
    athena_dionysus['name'] = '계산된 위험'
    athena_dionysus['condition'] =[['공격', '특공', '돌진', '지원'], ['공격', '특공', '돌진', '지원']]
    athena_dionysus['owner'] = {'아테나' : 0, '디오니소스' : 1}
    athena_dionysus['description'] = '적들의 원거리 발사체가 느려집니다.'
    athena_dionysus['is_selected'] = [False, False]
    data.append(athena_dionysus)

    athena_deme = {}
    athena_deme['name'] = '끈질긴 생명력'
    athena_deme['condition'] =[['공격', '특공', '탄환마법','섬광마법','돌진', '지원'], ['공격', '특공', '마법광선','마법섬광','돌진', '지원']]
    athena_deme['owner'] = {'아테나' : 0, '데메테르' : 1}
    athena_deme['description'] = '죽음 저항이 없을 때 체력이 천천히 차오릅니다.'
    athena_deme['is_selected'] = [False, False]
    data.append(athena_deme)

    apro_artemis = {}
    apro_artemis['name'] = '비통함'
    apro_artemis['condition'] =[['공격', '특공', '마법','돌진'], ['공격', '특공', '탄환마법2', '섬광마법2']]
    apro_artemis['owner'] = {'아프로디테' : 0, '아르테미스' : 1}
    apro_artemis['description'] = '치명타 효과는 약화된 적들에게 훨씬 더 높은 피해를 가합니다.'
    apro_artemis['is_selected'] = [False, False]
    data.append(apro_artemis)

    apro_ares = {}
    apro_ares['name'] = '갈망의 저주'
    apro_ares['condition'] =[['공격', '특공', '마법','돌진'], ['공격', '특공']]
    apro_ares['owner'] = {'아프로디테' : 0, '아레스' : 1}
    apro_ares['description'] = '파멸효과는 지속적으로 약화된 적들을 타격합니다.'
    apro_ares['is_selected'] = [False, False]
    data.append(apro_ares)

    apro_dionysus = {}
    apro_dionysus['name'] = '낮은 내성'
    apro_dionysus['condition'] =[['공격', '특공', '마법','돌진'], ['공격', '특공','돌진']]
    apro_dionysus['owner'] = {'아프로디테' : 0, '디오니소스' : 1}
    apro_dionysus['description'] = '숙취 효과는 약화된 적들을 상대로 더 많이 중첩될 수 있습니다.'
    apro_dionysus['is_selected'] = [False, False]
    data.append(apro_dionysus)

    apro_deme = {}
    apro_deme['name'] = '차가운 포옹'
    apro_deme['condition'] =[['공격', '특공', '돌진','지원'], ['마법광선']]
    apro_deme['owner'] = {'아프로디테' : 0, '데메테르' : 1}
    apro_deme['description'] = '마법 수정은 광선을 +4초동안 자그레우스에게 발사합니다.'
    apro_deme['is_selected'] = [False, False]
    data.append(apro_deme)


    artemis_ares = {}
    artemis_ares['name'] = '사냥하는 칼날'
    artemis_ares['condition'] =[['공격', '특공', '돌진', '지원'], ['마법']]
    artemis_ares['owner'] = {'아르테미스' : 0, '아레스' : 1}
    artemis_ares['description'] = '마법은 가장 가까운 적을 찾아가는 더 빠른 칼날 균열을 만듭니다.'
    artemis_ares['is_selected'] = [False, False]
    data.append(artemis_ares)

    artemis_dionysus = {}
    artemis_dionysus['name'] = '쪼개지는 두통'
    artemis_dionysus['condition'] =[['공격', '특공', '탄환마법2', '지원'], ['공격', '특공', '돌진', '지원']]
    artemis_dionysus['owner'] = {'아르테미스' : 0, '디오니소스' : 1}
    artemis_dionysus['description'] = '숙취에 시달리는 적은 치명타 피해를 입을 확률이 더 높아집니다.'
    artemis_dionysus['is_selected'] = [False, False]
    data.append(artemis_dionysus)

    artemis_deme = {}
    artemis_deme['name'] = '수정같은 선명함'
    artemis_deme['condition'] =[['공격', '특공', '돌진', '지원'], ['마법광선']]
    artemis_deme['owner'] = {'아르테미스' : 0, '데메테르' : 1}
    artemis_deme['description'] = '마법이 더 강해지고 적을 더 효과적으로 추적합니다.'
    artemis_deme['is_selected'] = [False, False]
    data.append(artemis_deme)

    ares_dionysus = {}
    ares_dionysus['name'] = '메스꺼움의 저주'
    ares_dionysus['condition'] =[['공격', '특공', '마법', '돌진', '지원'], ['공격', '특공', '돌진', '지원']]
    ares_dionysus['owner'] = {'아레스' : 0, '디오니소스' : 1}
    ares_dionysus['description'] = ''
    ares_dionysus['is_selected'] = [False, False]
    data.append(ares_dionysus)

    ares_deme = {}
    ares_deme['name'] = '결빙 소용돌이'
    ares_deme['condition'] =[['마법'], ['공격', '특공', '돌진', '지원']]
    ares_deme['owner'] = {'아레스' : 0, '데메테르' : 1}
    ares_deme['description'] = '숙취는 피해를 더 빨리 가합니다.'
    ares_deme['is_selected'] = [False, False]
    data.append(ares_deme)

    dionysus_deme = {}
    dionysus_deme['name'] = '얼음 포도주'
    dionysus_deme['condition'] =[['마법'], ['공격', '특공', '돌진', '지원']]
    dionysus_deme['owner'] = {'디오니소스' : 0, '데메테르' : 1}
    dionysus_deme['description'] = '마법은 범위안에 냉기를 입히는 축제 안개를 터트립니다.'
    dionysus_deme['is_selected'] = [False, False]
    data.append(dionysus_deme)

    with open('hades.json','w', encoding = 'utf-8') as json_file:
        json.dump(data, json_file, indent = '\t')


# In[1]:


def openJson():
    with open('hades.json','r') as f:
        hades = json.load(f)
    return hades

def selectItem(hades, god, ability):
    for duo in hades:
        for idx, val in enumerate(duo['owner']):
            if (val == god):
                for cond in duo['condition'][idx]:
                    if (ability == cond):
                         duo['is_selected'][idx] = True
        if ('마법' in ability):
            target = '마법'
        else:
            target = ability
     
        for i in range(2):
            result = []
            for cond in duo['condition'][i]:
                if (target in cond):
                    continue
                result.append(cond)
            duo['condition'][i] = result
                    
               

def is_selected(duo, index):
    if (duo['is_selected'][index] == True):
        return True
    return False
def is_possible(duo):
    A = duo['condition'][0]
    B = duo['condition'][1]
    condA = condB = False
    if(duo['is_selected'][0] == True or len(A) >= 1):
        condA = True
    if(duo['is_selected'][1] == True or len(B) >= 1):
        condB = True
    if (condA and condB):
            return True
    return False

def getAll(hades):
    result = []
    for duo in hades:
        if (is_possible(duo) == True):
            result.append(duo['name'])
    return result
def getSelected(hades):
    result = []
    for duo in hades:
        if (duo['is_selected'][0] == True and duo['is_selected'][1] == True ):
            result.append(duo['name'])
    return result

def getUnSelected(hades):
    result = []
    for duo in hades:
        if (duo['is_selected'][0] == True and duo['is_selected'][1] == True ):
            continue
        if (is_possible(duo) == True):
            result.append(duo['name'])
    return result

def resetHades():
    return openJson()

