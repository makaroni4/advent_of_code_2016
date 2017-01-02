from collections import defaultdict
import operator

def decode(signals):
  message = ""
  column_signals = zip(*signals)

  for signal in column_signals:
    chars = defaultdict(int)

    for char in signal:
      chars[char] += 1

    sorted_letters = sorted(chars.items(), key=operator.itemgetter(1), reverse=True)
    message += sorted_letters[0][0]

  return message

assert decode(["eedadn" ,"drvtee" ,"eandsr" ,"raavrd" ,"atevrs" ,"tsrnev" ,"sdttsa" ,"rasrtv" ,"nssdts" ,"ntnada" ,"svetve" ,"tesnvt" ,"vntsnd" ,"vrdear" ,"dvrsen" ,"enarar"]) == "easter"

signals = open("input.dat").read().strip().split("\n")
print decode(signals)
