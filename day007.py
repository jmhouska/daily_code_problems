# - Medium
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

def processMessage(message):
    print("message", message)
    possible = 0
    for i in range(len(message)):
        if i > 0:
            possible = decode(message[i:i+2]) + possible
    return possible + 1

def decode(value):
    value = int(value)
    if value < 27:
        return 1
    else:
        return 0  


def decode_cnt_no_zero(msg_list):
    if len(msg_list) <= 1:
        return 1

    if len(msg_list) >= 2:
        if 1 <= int(''.join(msg_list[0:2])) <= 26:
            return  (decode_cnt_no_zero(msg_list[1:]) +
                        decode_cnt_no_zero(msg_list[2:]))
        return decode_cnt_no_zero(msg_list[1:])


if __name__ == "__main__":
    # 1 - a
    message = '1'
    decoded = processMessage(message)
    print('options', decoded)
    # 11 - aa, k
    message = '11'
    decoded = processMessage(message)
    print('options', decoded)
    # 199 aii - si # 1919 aiai, ss, sai, ais
    print('m', processMessage('1919'))
    print(decode_cnt_no_zero('1919'))
    
    # 199 aii - si # 1919 aiai, ss, sai, ais
    print('m', processMessage('19198'))
    print(decode_cnt_no_zero('19198'))

    print('m', processMessage('81'))
    print(decode_cnt_no_zero('81'))

    print('m', processMessage('11'))
    print(decode_cnt_no_zero('11'))

    print('m', processMessage('111'))
    print(decode_cnt_no_zero('111'))

    print('m', processMessage('1111'))
    print(decode_cnt_no_zero('1111'))

    print('m', processMessage('1311'))
    print(decode_cnt_no_zero('1311'))
