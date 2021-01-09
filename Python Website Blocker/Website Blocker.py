the_hosts_file_path= r"C:\WINDOWS\System32\drivers\etc\hosts"
redirect="127.0.0.1"

websites_to_block = ["instagram.com", "www.instagram.com",
                    "www.facebook.com", "facebook.com"]
try:
    print('After the program ends the websites will be still blocked to unblock use the website unblocker.py file')
    print('-----------------')
         
    with open(the_hosts_file_path,'r+') as fi:
        con = fi.read()
        for i in websites_to_block:
            if i in con:
                pass
            else:
                fi.write('\n')
                fi.write(redirect+' '+i)
                print('done adding a site')
    print('Well done the websites are blocked now')
    print('Good Time (without the blocked websites -_-)\n=====================')
    exit()
            
except:
    print('bye if u want to restart rerun the program and if u want to delee the block use the unblocker -_-')    

