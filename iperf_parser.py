import re

def parser(output):
    result = []
    decode_output = output.read().decode('utf-8')
    reg_exp = re.compile(r'([0-9]*[.][0-9]+-\s?[0-9]*[.][0-9]+)|([0-9]*[.][0-9]+|[0-9]+)')

    for line in decode_output.split('\n'):
        matches = re.findall(reg_exp, line)

        if matches and len(matches) == 4:
            id, interval, transfer, bitrate = matches
            Interval = ''.join(interval)
            Transfer = float(''.join(transfer))
            Bitrate = float(''.join(bitrate))
            
            result.append({
                'Interval': Interval,
                'Transfer': Transfer,
                'Bitrate': Bitrate
            })

    return result