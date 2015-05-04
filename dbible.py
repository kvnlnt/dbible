#!/usr/bin/env python
import optparse

def main():
    p = optparse.OptionParser()

    # options
    p.add_option('--list', '-l',  help="list books")


    options, arguments = p.parse_args()
    print 'Hello %s' % options.person

if __name__ == '__main__':
    main()