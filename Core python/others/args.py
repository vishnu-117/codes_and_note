def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venue"))

print(concat("earth", "mars", "venue", sep="\\"))
