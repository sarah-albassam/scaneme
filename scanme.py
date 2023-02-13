import argparse
import sqli_scanner as sq

art = r'''
    ███████╗ ██████╗ █████╗ ███╗   ██╗    ███╗   ███╗███████╗
    ██╔════╝██╔════╝██╔══██╗████╗  ██║    ████╗ ████║██╔════╝
    ███████╗██║     ███████║██╔██╗ ██║    ██╔████╔██║█████╗
    ╚════██║██║     ██╔══██║██║╚██╗██║    ██║╚██╔╝██║██╔══╝
    ███████║╚██████╗██║  ██║██║ ╚████║    ██║ ╚═╝ ██║███████╗
    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝
'''
print(art)
print("--Credits: ")
print("[<3] Sarah Albassam")
print("[<3] Shahad AlGhareeb")
print("[<3] Shaima AlBaker")
print("[<3] Lama Almesned")
print("[<3] Maram Alnaim")

print("\n--> Instructor: Mr. Hussain Alattas\n\n")


def get_args():
    parser = argparse.ArgumentParser(prog='SCANME',
                                description=f'check all vulnerable websites in case one day you would use in future')
    parser.add_argument('-url', help='Target URL', type=str)
    parser.add_argument('-ls','--list', help='list all vulerable websites found',action='store_true')
    parser.add_argument('-sc','--sqliCrawl', help='crawl the url and scan sqli vulnerability',action='store_true')
    parser.add_argument('-t','--TimeTest', help='use the time test test for given url',action='store_true')

    return parser.parse_args()



args = get_args()

if args.url:
    sq.scan_sql_injection(args.url)

if args.list:
    sq.printi_list()

if args.url and args.TimeTest:
     sq.sql_Time(args.url)

if args.url and  args.sqliCrawl:
     sq.crawl(args.url)

sq.thank_you()