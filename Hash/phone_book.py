# python2

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(raw_input())
    return [Query(raw_input().split(' ')) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contactsNumbers = [None]*10000000

    for cur_query in queries:
        if cur_query.type == 'add':
            contactsNumbers[cur_query.number] = cur_query
        elif cur_query.type == 'del':
            contactsNumbers[cur_query.number] = None
        else:
            response = 'not found'
            if (contactsNumbers[cur_query.number] != None):
                response = contactsNumbers[cur_query.number].name
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

