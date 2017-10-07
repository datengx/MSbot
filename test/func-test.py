# Testing code


def hello(msg):
    print "Hello, " + msg


def main():
    import sys
    print "Script name is", sys.argv[0]
    if len(sys.argv)>=2:
        hello(sys.argv[1])
    else:
        hello("Please say something next time")


if __name__=='__main__':
    main()