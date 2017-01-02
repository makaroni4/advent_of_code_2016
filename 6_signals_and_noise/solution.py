from collections import defaultdict
import operator

def decode(signals, most_common=True):
  message = ""
  column_signals = zip(*signals)

  for signal in column_signals:
    chars = defaultdict(int)

    for char in signal:
      chars[char] += 1

    sorted_letters = sorted(chars.items(), key=operator.itemgetter(1), reverse=most_common)
    message += sorted_letters[0][0]

  return message

assert decode(["eedadn" ,"drvtee" ,"eandsr" ,"raavrd" ,"atevrs" ,"tsrnev" ,"sdttsa" ,"rasrtv" ,"nssdts" ,"ntnada" ,"svetve" ,"tesnvt" ,"vntsnd" ,"vrdear" ,"dvrsen" ,"enarar"], True) == "easter"

signals = open("input.dat").read().strip().split("\n")
print decode(signals, True)

assert decode(["eedadn" ,"drvtee" ,"eandsr" ,"raavrd" ,"atevrs" ,"tsrnev" ,"sdttsa" ,"rasrtv" ,"nssdts" ,"ntnada" ,"svetve" ,"tesnvt" ,"vntsnd" ,"vrdear" ,"dvrsen" ,"enarar"], False) == "advent"
print decode(signals, False)
