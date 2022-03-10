'''
https://www.codewars.com/kata/5ae840b8783bb4ef79000094/train/python
Level: 6kyu


Directions:


Your task is to implement a function that takes one or more dictionaries and combines them in one result dictionary.

The keys in the given dictionaries can overlap. In that case you should combine all source values in an array. Duplicate values should be preserved.

Here is an example:

source1 = {"A": 1, "B": 2} 
source2 = {"A": 3}

result = merge(source1, source2);
// result should have this content: {"A": [1, 3]}, "B": [2]}
You can assume that only valid dictionaries are passed to your function. The number of given dictionaries might be large. So take care about performance.


Tests:


def compare(actual, expected):
    sort = lambda x: x
    test.assert_equals(len(actual), len(expected), "The length of the result dictionary is not correct")
    for ka, va in actual.items():
        test.assert_equals(sorted(va, key=sort), sorted(expected[ka], key=sort), "The content of a dictionary item is not correct")

test.describe("Merge_EmptyDictionaries_Returns_Empty_Dictionary")
test.assert_equals(merge({},{},{}), {})

test.describe("Merge_Single_Dictionary_Returns_Dictionary_With_Same_Content")
compare(merge({"A": 1, "B": 2, "C": 3}), {"A": [1], "B": [2], "C": [3]})

test.describe("Merge_Two_Simple_Dictionaries_Returns_Combined_Dictionary")
compare(merge({"A": 1}, {"B": 2}), {"A": [1], "B": [2]})

test.describe("Merge_Two_Dictionaries_With_Multiple_Values_Returns_Combined_Dictionary")
compare(merge({"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5}), {"A": [1, 4], "B": [2], "C": [3], "D": [5]})
'''


def merge(*dicts):
    # Create output dictionary
    merged_dict = {}
    # Create set of all keys
    all_keys = set()
    # Get all unique keys across all dictionaries
    for item in dicts:
        all_keys.update(item.keys())
    # For each unique key:
    for key in all_keys:
        values = []
        # Iterate through all dictionaries and 
        for item in dicts:
            # If it has the key, collect the value in an array
            if key in item:
                values.append(item[key])
        # Then put the collected values in the merged dictionary
        merged_dict[key] = values
    return merged_dict

