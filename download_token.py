import requests
import sys
import re

def main(args):
    if len(args) < 2:
        print "usage: python download_token.py <console_url> <api_key>"
    auth = args[1]
    console = args[0]
    get_url = "{base}/api/v1/canarytokens/fetch?auth_token={auth}".format(
        base=console, auth=auth)
    resp = requests.get(get_url)
    resp_obj =  resp.json()
    print "Available tokens on your console"
    print "--------------------------------"
    print "kind\t\ttoken\t\t\tmemo"
    # import pdb; pdb.set_trace()
    for token in resp_obj['tokens']:
        print "{}\t\t{}\t\t{}".format(token['kind'], token['canarytoken'], token['memo'])
    print "--------------------------------"
    canarytoken = raw_input("Please enter canarytoken you want to download:")
    found_token = False
    for token in resp_obj['tokens']:
        if canarytoken == token['canarytoken']:
            found_token = True
    if not found_token:
        print "****** Bad canarytoken entered *******"
        exit(-1)
    download_url = "{base}/api/v1/canarytoken/download?auth_token={auth}&canarytoken={token}".format(
        base=console, auth=auth, token=canarytoken)
    resp = requests.get(download_url)
    import pdb;pdb.set_trace()
    fname = re.findall('filename=(.+)', resp.headers.get('content-disposition'))[0]
    print "Outputting file to filename: {}".format(fname)
    open(fname, 'wb').write(resp.content)

if __name__ == "__main__":
    main(sys.argv[1:])