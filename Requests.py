# /usr/bin/env python3.7
# -*- coding: utf-8 -*-
from random import randint
import re
import requests
import vk
from config import GROUP_ID, VK_API_ACCESS_TOKEN, VK_API_VERSION
from objects.DataBase import *
from objects.User import *
from objects.Chat import *
from objects.Marrieds import *
from objects.Stats import *
from objects.StatsUser import *
from objects.Settings import *
from objects.TypeSet import *
from objects.Texts import *
import locale
import datetime


class Requests:
    peer_id = 0

    def __init__(self):
        print("Requests init")
        self.api = vk.API(vk.Session(
            access_token=VK_API_ACCESS_TOKEN), v=VK_API_VERSION)

    def update_temp_data(self, peer_id, chat_id):
        self.peer_id = peer_id
        self.chat_id = chat_id

    def find_update_user(self, member_id):
        user = find_user(member_id)
        if len(user.full_name) == 0:
            user.full_name = self.api_full_name(user.id)
            user.save()

    def api_full_name(self, user_id):
        name = self.api.users.get(user_ids=user_id)[0]
        return "{0} {1}".format(name['first_name'], name['last_name'])

    def send_msg(self, msg):
        return self.api.messages.send(peer_id=self.peer_id, random_id=randint(
            -2147483647, 2147483647), message=msg)

    def remove_chat_user(self, id):
        if id == GROUP_ID:
            return False
        try:
            self.api.messages.removeChatUser(
                chat_id=self.chat_id, member_id=id)
            return True
        except vk.exceptions.VkAPIError:
            self.send_msg(msg='По какой-то причине нет доступа :(')
            return False

    def delete_msg(self, id):
        self.api.messages.delete(
            message_ids=str(id), delete_for_all=1, group_id=GROUP_ID)

    def getConversationsById(self):
        try:
            chat_data = self.api.messages.getConversationsById(
                peer_ids=self.peer_id, group_id=GROUP_ID)
            if chat_data['items']:
                if chat_data['items'][0]:
                    if chat_data['items'][0].get("chat_settings") and len(chat_data['items'][0]['chat_settings']) != 0:
                        return chat_data['items'][0]['chat_settings']
                    else:
                        return False
        except vk.exceptions.VkAPIError:
            return False

    def getConversationMembers(self):
        return self.api.messages.getConversationMembers(peer_id=self.peer_id, group_id=GROUP_ID)['profiles']
