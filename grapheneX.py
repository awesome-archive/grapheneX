#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.argparser import parse_cli_args
from core.utils.helpers import print_header, check_privileges, check_host_port,logger
from core.cli.shell import Shell
from core.web.server import *

def main():
    args = parse_cli_args()
    if(args['web']):
        host, port = parser_host_port(args['host_port'])
        try:
            app.run(host=host, port=port)
        except:
            logger.error("Invalid Host & Port info")
            logger.info('Using default (host:0.0.0.0, port:8080)')
            app.run(host='0.0.0.0', port='8080')
    else:
    	print_header()
    	check_privileges()
    	shell = Shell()
    	try:
    		shell.cmdloop()
    	except KeyboardInterrupt:
    		shell.do_EOF(None)

if __name__ == "__main__":
    main()