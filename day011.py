# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

def hasPrefix(prefix, items):
    prefixLength = len(prefix)
    prefixed = []
    for i in items:
        if prefix == i[:prefixLength]:
            prefixed.append(i)
    return prefixed

def preProcessList(items):
    newItems = {}
    for i in items:
        if i[0] not in newItems:
            newItems[i[0]] = []
        newItems[i[0]].append(i)
    return newItems

if __name__ == "__main__":
    items = ['dog', 'deer', 'deal']
    prefix = 'de'
    # raw list search
    prefixed = hasPrefix(prefix, items)
    print(prefixed)
    # preprocessing items for the hint
    processedItems = preProcessList(items)
    hasPrefixed = hasPrefix(prefix, processedItems[prefix[0]])
    print(hasPrefixed)
