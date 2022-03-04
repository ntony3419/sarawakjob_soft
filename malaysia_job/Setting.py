
import configparser
import os
import csv
class Setting(object):
    def __init__(self):
        super().__init__()
        self.fb_acc = self.fb_acc_list("FB_CHROME_profile_accounts.csv")
        self.setting = self.load_setting()
        self.xpaths=self.load_xpath()





    def load_setting(self):
        setting={}
        self.config = configparser.ConfigParser()
        try:
            config_file = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
            self.config.read(os.path.join(config_file, 'setting.conf'))
        except Exception:
            print("error reading config file")

        setting["CONTENT_CSV"] = self.config["DEFAULT"]["CONTENT_CSV"]
        setting["CONTENT_TXT"] = self.config["DEFAULT"]["CONTENT_TXT"]
        setting["CONTENT_XLS"] = self.config["DEFAULT"]["CONTENT_XLS"]
        setting["JOB_FILE"] = self.config["DEFAULT"]["JOB_FILE"]

        setting["DATABASE_ADDRESS"] = self.config["DATABASE"]["DATABASE_ADDRESS"]
        setting["DATABASE_NAME"] = self.config["DATABASE"]["DATABASE_NAME"]
        setting["USER_NAME"] = self.config["DATABASE"]["USER_NAME"]
        setting["PASSWORD"] = self.config["DATABASE"]["PASSWORD"]

        setting["DRIVER_PATH"] = self.config["CHROME"]["DRIVER_PATH"]

        setting["CHROME_USER_AGENT"] = None
        if  self.config["CHROME"]["CHROME_USER_AGENT"] != "none" or self.config["CHROME"]["CHROME_USER_AGENT"] != "":
            setting["CHROME_USER_AGENT"] = self.config["CHROME"]["CHROME_USER_AGENT"]



        # load dict of facebook account



        setting["FB_MULTIPLE_ACC"] = False
        if self.config["FACEBOOK"]["FB_MULTIPLE_ACC"].lower() == "true":
            setting["FB_MULTIPLE_ACC"] = True
        setting["PROFILE_PATH"] = None
        if setting["FB_MULTIPLE_ACC"] is False:
            setting["FANPAGE_ID"] = self.fb_acc[0]["FANPAGE_ID"]
            setting["GROUP_TO_SHARE"] = int(self.fb_acc[0]["GROUP_TO_SHARE"])
            setting["FRIEND_TO_ADD"] = int(self.fb_acc[0]["FRIEND_TO_ADD"])
            setting["FRIEND_TO_CONFIRM"] =int(self.fb_acc[0]["FRIEND_TO_CONFIRM"])
            '''chrome'''
            setting["PROFILE_PATH"] = self.fb_acc[0]["CHROME_PROFILE_PATH"]
            setting["PROFILE_NUMBER"] = self.fb_acc[0]["CHROME_PROFILE_NUMBER"]

        setting["WP_USERNAME"] = self.config["WORDPRESS"]["WP_USERNAME"]

        setting["WP_PASSWORD"] = self.config["WORDPRESS"]["WP_PASSWORD"].replace("\"","")

        return setting

    def load_xpath(self):
        xpaths={}
        self.config = configparser.ConfigParser()
        try:
            config_file = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
            self.config.read(os.path.join(config_file, 'xpaths.conf'))
        except Exception:
            print("error reading config file")

        xpaths["GROUP_CREATE_POST_BTN"] = self.config["FACEBOOK_GROUP"]["GROUP_CREATE_POST_BTN"]
        xpaths["GROUP_TEXT_FIELD"] = self.config["FACEBOOK_GROUP"]["GROUP_TEXT_FIELD"]
        xpaths["GROUP_POST_BTN"] = self.config["FACEBOOK_GROUP"]["GROUP_POST_BTN"]

        xpaths["FANPAGE_CREATE_POST_BTN"] = self.config["FACEBOOK_FANPAGE"]["FANPAGE_CREATE_POST_BTN"]
        xpaths["FANPAGE_TEXT_FIELD"] = self.config["FACEBOOK_FANPAGE"]["FANPAGE_TEXT_FIELD"]
        xpaths["FANPAGE_POST_BTN"] = self.config["FACEBOOK_FANPAGE"]["FANPAGE_POST_BTN"]

        xpaths["WALL_CREATE_POST_BTN"] = self.config["FACEBOOK_PERSONAL_WALL"]["WALL_CREATE_POST_BTN"]
        xpaths["WALL_TEXT_FIELD"] = self.config["FACEBOOK_PERSONAL_WALL"]["WALL_TEXT_FIELD"]
        xpaths["WALL_POST_BTN"] = self.config["FACEBOOK_PERSONAL_WALL"]["WALL_POST_BTN"]

        xpaths["NEWS_FEED_CREATE_POST_BTN"] = self.config["FACEBOOK_NEWS_FEED"]["NEWS_FEED_CREATE_POST_BTN"]
        xpaths["NEWS_FEED_TEXT_FIELD"] = self.config["FACEBOOK_NEWS_FEED"]["NEWS_FEED_TEXT_FIELD"]
        xpaths["NEWS_FEED_POST_BTN"] = self.config["FACEBOOK_NEWS_FEED"]["NEWS_FEED_POST_BTN"]

        xpaths["FRIEND_ADD_BTN"] = self.config["FACEBOOK_FRIEND"]["FRIEND_ADD_BTN"]
        xpaths["FRIEND_CONFIRM_BTN"] = self.config["FACEBOOK_FRIEND"]["FRIEND_CONFIRM_BTN"]


        return xpaths

    def fb_acc_list(self, file_name):
        input_file = csv.DictReader(open(file_name))
        acc_dict = {}
        count=0
        for row in input_file:
            acc_dict[count]=row
            count +=1
        return acc_dict

# setting = Setting()
# accs= setting.fb_acc_list(r"C:\Users\quang nguyen\PycharmProjects\python\facebook_auto\FB_CHROME_profile_accounts.csv")
#
# print(len(accs))
#print(accs[0]["FANPAGE_ID"])