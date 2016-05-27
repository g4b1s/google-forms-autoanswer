import mechanize, sys


link = 'https://docs.google.com/forms/d/1a6UqltG8Rg66MCRynzVuWs-qQhoNFB_HVJ1aTyVsUrI/viewform'
rsp = ['x', 'x']


def vota(i):
	br = mechanize.Browser()
	br.open(link)
	br.set_handle_robots(False)
	br.form = list(br.forms())[0]

    
	for control in br.form.controls:
		if 'en' in control.name:
		    control.readonly = False
		    control.disabled = False

		    br[control.name] = rsp[i]
		    i+=1
		    # print control
		    # print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])
	
	br.submit()
	br.close()

def main():
	i=0
	vota(i)



main()