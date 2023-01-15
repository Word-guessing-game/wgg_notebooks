import json

def assertJsonEqual(first = {}, second = {}):
    first_result = json.dumps(first, sort_keys=True)
    second_result = json.dumps(second, sort_keys=True)
    assert first_result == second_result

def assertListOfJsonEqual(first = [], second = []):
    first_result = list(sorted(map(lambda x: json.dumps(x, sort_keys=True), first)))
    second_result = list(sorted(map(lambda x: json.dumps(x, sort_keys=True), second)))
    print(f'{first_result=}')
    print(f'{second_result=}')
    assert first_result == second_result
