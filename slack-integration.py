import requests
import sys

'''
Your web or mobile app should redirect users to the following URL:

https://slack.com/oauth/authorize

The following values should be passed as GET parameters:

client_id - issued when you created your app (required)
scope - permissions to request (see below) (required)
redirect_uri - URL to redirect back to (see below) (optional)
state - unique string to be passed back upon completion (optional)
team - Slack team ID of a workspace to attempt to restrict to (optional)

You may need an oauth token:
xoxp-843832539249-840885641715-854257848917-6858d4d0ef49f74e6a5118bb2a619439
'''

def main(args):
	payload={
		'client_id':'client_id_here',
		'scope':'incoming-webhook',
		'state':'aUniqueStringYesNo',
		'team':'T062N4QR1'
	}
	step1_url='https://slack.com/oauth/authorize'

	resp = requests.get(step1_url, params=payload)


if __name__ == "__main__":
	main(sys.argv[1:])
