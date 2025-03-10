# 解析课上的抖音数据中每一个作品的音乐信息，将所有的作品的music的作者，title以及播放的url，三个信息放在一个元组中，所有作品对应元组放在大列表中。
data = {
    "status_code": 0,
    "min_cursor": 0,
    "max_cursor": 1705208149000,
    "has_more": 1,
    "aweme_list": [
        {
            "aweme_id": "7473365621061733641",
            "desc": "想我们了吗",
            "create_time": 1740028553,
            "author": {
                "uid": "3548856441386627",
                "ban_user_functions": None,
                "nickname": "小苏菲Yomi",
                "cf_list": None,
                "link_item_list": None,
                "avatar_thumb": {
                    "uri": "100x100/aweme-avatar/tos-cn-avt-0015_e586aa279259812ff17c84d58dcd7f7a",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_e586aa279259812ff17c84d58dcd7f7a.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "avatar_schema_list": None,
                "signature_extra": None,
                "follow_status": 0,
                "risk_notice_text": "",
                "private_relation_list": None,
                "follower_list_secondary_information_struct": None,
                "custom_verify": "",
                "can_set_geofencing": None,
                "batch_unfollow_contain_tabs": None,
                "display_info": None,
                "verification_permission_ids": None,
                "need_points": None,
                "share_info": {
                    "share_url": "",
                    "share_weibo_desc": "",
                    "share_desc": "",
                    "share_title": "",
                    "share_qrcode_url": {
                        "uri": "2e465000801715cb87430",
                        "url_list": [
                            "https://p3-pc-sign.douyinpic.com/obj/2e465000801715cb87430?lk3s=138a59ce&x-expires=1740495600&x-signature=VLET5Kqlj%2Bzz76z6PjTwcsQA7mM%3D&from=327834062",
                            "https://p9-pc-sign.douyinpic.com/obj/2e465000801715cb87430?lk3s=138a59ce&x-expires=1740495600&x-signature=G4rxLZLC8R9dqRfORvRhgI%2BkpW4%3D&from=327834062"
                        ],
                        "width": 720,
                        "height": 720
                    },
                    "share_title_myself": "",
                    "share_title_other": "",
                    "share_desc_info": ""
                },
                "familiar_visitor_user": None,
                "homepage_bottom_toast": None,
                "batch_unfollow_relation_desc": None,
                "enterprise_verify_reason": "",
                "is_ad_fake": False,
                "account_cert_info": "{}",
                "card_entries_not_display": None,
                "user_tags": None,
                "profile_mob_params": None,
                "card_sort_priority": None,
                "not_seen_item_id_list": None,
                "card_entries": None,
                "prevent_download": False,
                "text_extra": None,
                "sec_uid": "MS4wLjABAAAA0HwZJN6-JDCSTjxiMk-czhyZWxes8XIDEjppFXExauK8-kQTLMEH9ZdfIXxnl9tS",
                "im_role_ids": None,
                "follower_status": 0,
                "not_seen_item_id_list_v2": None,
                "contrail_list": None,
                "data_label_list": None,
                "cover_url": [
                    {
                        "uri": "c8510002be9a3a61aad2",
                        "url_list": [
                            "https://p3-pc-sign.douyinpic.com/obj/c8510002be9a3a61aad2?lk3s=138a59ce&x-expires=1741683600&x-signature=EFWLy4VShefql8py2jCihCNLrr4%3D&from=327834062",
                            "https://p9-pc-sign.douyinpic.com/obj/c8510002be9a3a61aad2?lk3s=138a59ce&x-expires=1741683600&x-signature=jVI%2FKFrse7iVVzpzakMSFh%2BWQnU%3D&from=327834062"
                        ],
                        "width": 720,
                        "height": 720
                    }
                ],
                "user_permissions": None,
                "offline_info_list": None,
                "endorsement_info_list": None,
                "interest_tags": None,
                "personal_tag_list": None,
                "white_cover_url": None,
                "creator_tag_list": None,
                "special_people_labels": None
            },
            "music": {
                "id": 7351016366839253000,
                "id_str": "7351016366839253018",
                "title": "弹给路小雨的吉他（剪辑版）",
                "author": "Jazzzcz",
                "album": "",
                "cover_hd": {
                    "uri": "tos-cn-v-2774c002/oQazbABxEAAiAD6ZfWBQENAiKdbRSS74C09shv",
                    "url_list": [
                        "https://p26.douyinpic.com/aweme/1080x1080/tos-cn-v-2774c002/oQazbABxEAAiAD6ZfWBQENAiKdbRSS74C09shv.jpeg",
                        "https://p11.douyinpic.com/aweme/1080x1080/tos-cn-v-2774c002/oQazbABxEAAiAD6ZfWBQENAiKdbRSS74C09shv.jpeg"
                    ],
                    "width": 720,
                    "height": 720
                },
                "cover_large": {
                    "uri": "tos-cn-v-2774c002/oQazbABxEAAiAD6ZfWBQENAiKdbRSS74C09shv",
                    "url_list": [
                        "https://p26.douyinpic.com/aweme/720x720/tos-cn-v-2774c002/oQazbABxEAAiAD6ZfWBQENAiKdbRSS74C09shv.jpeg",
                        "https://p11.douyinpic.com/aweme/720x720/tos-cn-v-2774c002/oQazbABxEAAiAD6ZfWBQENAiKdbRSS74C09shv.jpeg"
                    ],
                    "width": 720,
                    "height": 720
                },
                "cover_medium": {
                    "uri": "tos-cn-v-2774c002/oQazbABxEAAiAD6ZfWBQENAiKdbRSS74C09shv",
                    "url_list": [
                        "https://p26.douyinpic.com/aweme/200x200/tos-cn-v-2774c002/oQazbABxEAAiAD6ZfWBQENAiKdbRSS74C09shv.jpeg",
                        "https://p11.douyinpic.com/aweme/200x200/tos-cn-v-2774c002/oQazbABxEAAiAD6ZfWBQENAiKdbRSS74C09shv.jpeg"
                    ],
                    "width": 720,
                    "height": 720
                },
                "cover_thumb": {
                    "uri": "tos-cn-v-2774c002/oQazbABxEAAiAD6ZfWBQENAiKdbRSS74C09shv",
                    "url_list": [
                        "https://p26.douyinpic.com/aweme/100x100/tos-cn-v-2774c002/oQazbABxEAAiAD6ZfWBQENAiKdbRSS74C09shv.jpeg",
                        "https://p11.douyinpic.com/aweme/100x100/tos-cn-v-2774c002/oQazbABxEAAiAD6ZfWBQENAiKdbRSS74C09shv.jpeg"
                    ],
                    "width": 720,
                    "height": 720
                },
                "play_url": {
                    "uri": "https://sf3-cdn-tos.douyinstatic.com/obj/tos-cn-ve-2774/oo7e8tBoI6ZCsHCCTbBfEMN9mc20hnqpBQDgCA",
                    "url_list": [
                        "https://sf3-cdn-tos.douyinstatic.com/obj/tos-cn-ve-2774/oo7e8tBoI6ZCsHCCTbBfEMN9mc20hnqpBQDgCA",
                        "https://sf5-hl-cdn-tos.douyinstatic.com/obj/tos-cn-ve-2774/oo7e8tBoI6ZCsHCCTbBfEMN9mc20hnqpBQDgCA"
                    ],
                    "width": 720,
                    "height": 720,
                    "url_key": "7351016366839253018"
                },
                "schema_url": "",
                "source_platform": 25,
                "start_time": 0,
                "end_time": 0,
                "duration": 185,
                "extra": "{\"is_subsidy_exp\":False,\"music_label_id\":1112,\"aggregate_exempt_conf\":[],\"peak\":\"0.9891244\",\"hit_high_follow_extend\":False,\"beats\":{\"audio_effect_onset\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/oI8BAxnbAP5m8ACpI7c8Zn0ngDgtNfAtfqBXIA\",\"beats_tracker\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/ow7BnbAntDWDIcn84AmgeBwPIHZ8CAlmAAfA8k\",\"energy_trace\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/o0AMAbDTnAAmeAytnHDz8BEuBBNEGe0gYdZn7C\",\"merged_beats\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/owMGzmAANCBSAZz0tuTHdGEgEfZieB3A2NhEAY\"},\"music_tagging\":{\"Languages\":[\"non_vocal\"],\"Moods\":[\"Calm\"],\"Genres\":[\"Easy Listening\"],\"Themes\":[\"Rainy\",\"Evening\"],\"AEDs\":[\"non_vocal\"],\"SingingVersions\":None,\"Instruments\":None},\"is_aed_music\":0,\"reviewed\":1,\"is_red\":0,\"hotsoon_review_time\":-1,\"cover_colors\":{\"rgb\":[24,19,13]},\"with_aed_model\":0,\"loudness\":\"-13.123918\",\"dsp_switch\":0,\"douyin_beats_info\":{},\"image_beats_url\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/ow7BnbAntDWDIcn84AmgeBwPIHZ8CAlmAAfA8k\",\"schedule_search_time\":0,\"is_high_follow_user\":False,\"hit_high_follow_original\":False,\"hit_high_follow_auto\":False,\"has_edited\":0,\"review_unshelve_reason\":0}",
                "user_count": 0,
                "position": None,
                "collect_stat": 0,
                "status": 1,
                "offline_desc": "",
                "owner_id": "91558135712",
                "owner_nickname": "",
                "is_original": True,
                "mid": "7351016366839253018",
                "binded_challenge_id": 0,
                "redirect": False,
                "is_restricted": False,
                "author_deleted": False,
                "is_del_video": False,
                "is_video_self_see": False,
                "owner_handle": "",
                "author_position": None,
                "prevent_download": False,
                "strong_beat_url": {
                    "uri": "https://sf3-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/o0EAinztXBhAwgZ4mBECCFEANEDyVoAUffoV1C",
                    "url_list": [
                        "https://sf3-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/o0EAinztXBhAwgZ4mBECCFEANEDyVoAUffoV1C",
                        "https://sf5-hl-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/o0EAinztXBhAwgZ4mBECCFEANEDyVoAUffoV1C"
                    ],
                    "width": 720,
                    "height": 720
                },
                "unshelve_countries": None,
                "prevent_item_download_status": 0,
                "external_song_info": [],
                "sec_uid": "MS4wLjABAAAANmD2JYSTMC5FkS6uSJjWx6fjtPzSeDKi-zT40ksCHpY",
                "avatar_thumb": {
                    "uri": "100x100/aweme-avatar/tos-cn-avt-0015_2a406777dfb5e6f6e1b681bce0aacc30",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_2a406777dfb5e6f6e1b681bce0aacc30.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "avatar_medium": {
                    "uri": "720x720/aweme-avatar/tos-cn-avt-0015_2a406777dfb5e6f6e1b681bce0aacc30",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_2a406777dfb5e6f6e1b681bce0aacc30.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "avatar_large": {
                    "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_2a406777dfb5e6f6e1b681bce0aacc30",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_2a406777dfb5e6f6e1b681bce0aacc30.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "preview_start_time": 139.967,
                "preview_end_time": 0,
                "is_commerce_music": False,
                "is_original_sound": False,
                "audition_duration": 185,
                "shoot_duration": 185,
                "reason_type": 0,
                "artists": [
                    {
                        "uid": "91558135712",
                        "sec_uid": "MS4wLjABAAAANmD2JYSTMC5FkS6uSJjWx6fjtPzSeDKi-zT40ksCHpY",
                        "nick_name": "Jazzzcz",
                        "handle": "Jazzzcz",
                        "avatar": {
                            "uri": "168x168/aweme-avatar/tos-cn-avt-0015_2a406777dfb5e6f6e1b681bce0aacc30",
                            "url_list": [
                                "https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_2a406777dfb5e6f6e1b681bce0aacc30~c5_168x168.jpeg?from=327834062"
                            ]
                        },
                        "is_verified": True,
                        "enter_type": 1
                    }
                ],
                "lyric_short_position": None,
                "mute_share": False,
                "tag_list": None,
                "dmv_auto_show": False,
                "is_pgc": True,
                "is_matched_metadata": False,
                "is_audio_url_with_cookie": False,
                "music_chart_ranks": None,
                "can_background_play": True,
                "music_status": 1,
                "video_duration": 6000,
                "pgc_music_type": 2,
                "cover_color_hsv": {
                    "h": 33,
                    "s": 35,
                    "v": 9
                },
                "author_status": 1,
                "search_impr": {
                    "entity_id": "7351016366839253018"
                },
                "song": {
                    "id": 7351016366839220000,
                    "id_str": "7351016366839220250",
                    "title": "弹给路小雨的吉他",
                    "artists": None,
                    "chorus": {
                        "start_ms": 140736,
                        "duration_ms": 184704
                    },
                    "chorus_v3_infos": None
                },
                "artist_user_infos": None,
                "dsp_status": 0,
                "musician_user_infos": None,
                "music_image_beats": {
                    "music_image_beats_url": {
                        "uri": "tos-cn-v-2774c002/ow7BnbAntDWDIcn84AmgeBwPIHZ8CAlmAAfA8k",
                        "url_list": [
                            "https://sf5-hl-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/ow7BnbAntDWDIcn84AmgeBwPIHZ8CAlmAAfA8k"
                        ],
                        "width": 720,
                        "height": 720
                    }
                },
                "music_collect_count": 0,
                "music_cover_atmosphere_color_value": ""
            }
        },
        {
            "aweme_id": "7408830973296626979",
            "desc": "每天陪你聊到凌晨和你说晚安的又是谁呢",
            "create_time": 1725002906,
            "author": {
                "uid": "3548856441386627",
                "ban_user_functions": None,
                "nickname": "小苏菲Yomi",
                "cf_list": None,
                "link_item_list": None,
                "avatar_thumb": {
                    "uri": "100x100/aweme-avatar/tos-cn-avt-0015_e586aa279259812ff17c84d58dcd7f7a",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_e586aa279259812ff17c84d58dcd7f7a.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "avatar_schema_list": None,
                "signature_extra": None,
                "follow_status": 0,
                "risk_notice_text": "",
                "private_relation_list": None,
                "follower_list_secondary_information_struct": None,
                "custom_verify": "",
                "can_set_geofencing": None,
                "batch_unfollow_contain_tabs": None,
                "display_info": None,
                "verification_permission_ids": None,
                "need_points": None,
                "share_info": {
                    "share_url": "",
                    "share_weibo_desc": "",
                    "share_desc": "",
                    "share_title": "",
                    "share_qrcode_url": {
                        "uri": "2e465000801715cb87430",
                        "url_list": [
                            "https://p3-pc-sign.douyinpic.com/obj/2e465000801715cb87430?lk3s=138a59ce&x-expires=1740495600&x-signature=VLET5Kqlj%2Bzz76z6PjTwcsQA7mM%3D&from=327834062",
                            "https://p9-pc-sign.douyinpic.com/obj/2e465000801715cb87430?lk3s=138a59ce&x-expires=1740495600&x-signature=G4rxLZLC8R9dqRfORvRhgI%2BkpW4%3D&from=327834062"
                        ],
                        "width": 720,
                        "height": 720
                    },
                    "share_title_myself": "",
                    "share_title_other": "",
                    "share_desc_info": ""
                },
                "familiar_visitor_user": None,
                "homepage_bottom_toast": None,
                "batch_unfollow_relation_desc": None,
                "enterprise_verify_reason": "",
                "is_ad_fake": False,
                "account_cert_info": "{}",
                "card_entries_not_display": None,
                "user_tags": None,
                "profile_mob_params": None,
                "card_sort_priority": None,
                "not_seen_item_id_list": None,
                "card_entries": None,
                "prevent_download": False,
                "text_extra": None,
                "sec_uid": "MS4wLjABAAAA0HwZJN6-JDCSTjxiMk-czhyZWxes8XIDEjppFXExauK8-kQTLMEH9ZdfIXxnl9tS",
                "im_role_ids": None,
                "follower_status": 0,
                "not_seen_item_id_list_v2": None,
                "contrail_list": None,
                "data_label_list": None,
                "cover_url": [
                    {
                        "uri": "c8510002be9a3a61aad2",
                        "url_list": [
                            "https://p3-pc-sign.douyinpic.com/obj/c8510002be9a3a61aad2?lk3s=138a59ce&x-expires=1741683600&x-signature=EFWLy4VShefql8py2jCihCNLrr4%3D&from=327834062",
                            "https://p9-pc-sign.douyinpic.com/obj/c8510002be9a3a61aad2?lk3s=138a59ce&x-expires=1741683600&x-signature=jVI%2FKFrse7iVVzpzakMSFh%2BWQnU%3D&from=327834062"
                        ],
                        "width": 720,
                        "height": 720
                    }
                ],
                "user_permissions": None,
                "offline_info_list": None,
                "endorsement_info_list": None,
                "interest_tags": None,
                "personal_tag_list": None,
                "white_cover_url": None,
                "creator_tag_list": None,
                "special_people_labels": None
            },
            "music": {
                "id": 6795558737597222000,
                "id_str": "6795558737597221645",
                "title": "@猪有蹄va创作的原声",
                "author": "猪有蹄va",
                "album": "",
                "cover_hd": {
                    "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "cover_large": {
                    "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "cover_medium": {
                    "uri": "720x720/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "cover_thumb": {
                    "uri": "100x100/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "play_url": {
                    "uri": "https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/1659074002767895.mp3",
                    "url_list": [
                        "https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/1659074002767895.mp3",
                        "https://sf3-cdn-tos.douyinstatic.com/obj/ies-music/1659074002767895.mp3"
                    ],
                    "width": 720,
                    "height": 720,
                    "url_key": "6795558737597221645"
                },
                "schema_url": "",
                "source_platform": 23,
                "start_time": 0,
                "end_time": 0,
                "duration": 20,
                "extra": "{\"is_aed_music\":1,\"is_high_follow_user\":False,\"hit_high_follow_auto\":False,\"dsp_switch\":0,\"has_edited\":0,\"image_beats_url\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1659136077690887\",\"beats\":{\"energy_trace\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1659136073058318\",\"merged_beats\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1659136077711374\",\"audio_effect_onset\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1659136073090062\",\"beats_tracker\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1659136077690887\"},\"uniqa_speech_score\":0.04,\"hit_high_follow_extend\":False,\"reviewed\":0,\"is_red\":0,\"aed_music_score\":0.02,\"aed_singing_score\":0.94,\"cover_colors\":None,\"is_subsidy_exp\":False,\"music_label_id\":None,\"extract_item_id\":6795622420897156367,\"review_unshelve_reason\":0,\"douyin_beats_info\":{},\"schedule_search_time\":0,\"hotsoon_review_time\":-1,\"music_tagging\":{\"Languages\":[\"Chinese\"],\"Moods\":[\"Dynamic\"],\"Genres\":[\"Others\"],\"Themes\":[\"No Theme\"],\"AEDs\":[\"Vocal\"],\"SingingVersions\":None,\"Instruments\":None},\"aggregate_exempt_conf\":[],\"with_aed_model\":1,\"hit_high_follow_original\":False}",
                "user_count": 0,
                "position": None,
                "collect_stat": 0,
                "status": 1,
                "offline_desc": "",
                "owner_id": "57393079210",
                "owner_nickname": "猪有蹄va",
                "is_original": False,
                "mid": "6795558737597221645",
                "binded_challenge_id": 0,
                "redirect": False,
                "is_restricted": False,
                "author_deleted": False,
                "is_del_video": False,
                "is_video_self_see": False,
                "owner_handle": "123zytbb",
                "author_position": None,
                "prevent_download": False,
                "strong_beat_url": {
                    "uri": "https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/pattern/2aa68f1d1cf91343f145c3d985f0467c.json",
                    "url_list": [
                        "https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/pattern/2aa68f1d1cf91343f145c3d985f0467c.json",
                        "https://sf3-cdn-tos.douyinstatic.com/obj/ies-music/pattern/2aa68f1d1cf91343f145c3d985f0467c.json"
                    ],
                    "width": 720,
                    "height": 720
                },
                "unshelve_countries": None,
                "prevent_item_download_status": 0,
                "external_song_info": [],
                "sec_uid": "MS4wLjABAAAAvPPxdd0Mwj8FpnyTMPEab5WPKq1Q3FLdp0sMIEIJmOM",
                "avatar_thumb": {
                    "uri": "100x100/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "avatar_medium": {
                    "uri": "720x720/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "avatar_large": {
                    "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_205c084235decaea346fd3ac1c6aa111.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "preview_start_time": 0,
                "preview_end_time": 0,
                "is_commerce_music": False,
                "is_original_sound": True,
                "audition_duration": 20,
                "shoot_duration": 20,
                "reason_type": 0,
                "artists": [],
                "lyric_short_position": None,
                "mute_share": False,
                "tag_list": None,
                "dmv_auto_show": False,
                "is_pgc": False,
                "is_matched_metadata": False,
                "is_audio_url_with_cookie": False,
                "matched_pgc_sound": {
                    "author": "精彩轩迪",
                    "title": "落日归山海",
                    "mixed_title": "",
                    "mixed_author": "",
                    "cover_medium": {
                        "uri": "tos-cn-v-2774c002/7fd857eb481447d6aa75f5767cb534e3",
                        "url_list": [
                            "https://p3.douyinpic.com/aweme/200x200/tos-cn-v-2774c002/7fd857eb481447d6aa75f5767cb534e3.jpeg",
                            "https://p11.douyinpic.com/aweme/200x200/tos-cn-v-2774c002/7fd857eb481447d6aa75f5767cb534e3.jpeg",
                            "https://p26.douyinpic.com/aweme/200x200/tos-cn-v-2774c002/7fd857eb481447d6aa75f5767cb534e3.jpeg"
                        ],
                        "width": 720,
                        "height": 720
                    }
                },
                "music_chart_ranks": None,
                "can_background_play": True,
                "music_status": 1,
                "video_duration": 20,
                "pgc_music_type": 2,
                "author_status": 1,
                "search_impr": {
                    "entity_id": "6795558737597221645"
                },
                "song": {
                    "id": 7071308509735815000,
                    "id_str": "7071308509735815204",
                    "artists": None,
                    "chorus_v3_infos": None
                },
                "artist_user_infos": None,
                "dsp_status": 10,
                "musician_user_infos": None,
                "music_image_beats": {
                    "music_image_beats_url": {
                        "uri": "ies-music/strong_beat/v3/1659136077690887",
                        "url_list": [
                            "https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1659136077690887"
                        ],
                        "width": 720,
                        "height": 720
                    }
                },
                "music_collect_count": 0,
                "music_cover_atmosphere_color_value": ""
            }
        },
        {
            "aweme_id": "7404374334673882408",
            "desc": "自己剪完都想笑哈哈哈哈哈哈哈哈哈哈",
            "create_time": 1723965255,
            "author": {
                "uid": "3548856441386627",
                "ban_user_functions": None,
                "nickname": "小苏菲Yomi",
                "cf_list": None,
                "link_item_list": None,
                "avatar_thumb": {
                    "uri": "100x100/aweme-avatar/tos-cn-avt-0015_e586aa279259812ff17c84d58dcd7f7a",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_e586aa279259812ff17c84d58dcd7f7a.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "avatar_schema_list": None,
                "signature_extra": None,
                "follow_status": 0,
                "risk_notice_text": "",
                "private_relation_list": None,
                "follower_list_secondary_information_struct": None,
                "custom_verify": "",
                "can_set_geofencing": None,
                "batch_unfollow_contain_tabs": None,
                "display_info": None,
                "verification_permission_ids": None,
                "need_points": None,
                "share_info": {
                    "share_url": "",
                    "share_weibo_desc": "",
                    "share_desc": "",
                    "share_title": "",
                    "share_qrcode_url": {
                        "uri": "2e465000801715cb87430",
                        "url_list": [
                            "https://p3-pc-sign.douyinpic.com/obj/2e465000801715cb87430?lk3s=138a59ce&x-expires=1740495600&x-signature=VLET5Kqlj%2Bzz76z6PjTwcsQA7mM%3D&from=327834062",
                            "https://p9-pc-sign.douyinpic.com/obj/2e465000801715cb87430?lk3s=138a59ce&x-expires=1740495600&x-signature=G4rxLZLC8R9dqRfORvRhgI%2BkpW4%3D&from=327834062"
                        ],
                        "width": 720,
                        "height": 720
                    },
                    "share_title_myself": "",
                    "share_title_other": "",
                    "share_desc_info": ""
                },
                "familiar_visitor_user": None,
                "homepage_bottom_toast": None,
                "batch_unfollow_relation_desc": None,
                "enterprise_verify_reason": "",
                "is_ad_fake": False,
                "account_cert_info": "{}",
                "card_entries_not_display": None,
                "user_tags": None,
                "profile_mob_params": None,
                "card_sort_priority": None,
                "not_seen_item_id_list": None,
                "card_entries": None,
                "prevent_download": False,
                "text_extra": None,
                "sec_uid": "MS4wLjABAAAA0HwZJN6-JDCSTjxiMk-czhyZWxes8XIDEjppFXExauK8-kQTLMEH9ZdfIXxnl9tS",
                "im_role_ids": None,
                "follower_status": 0,
                "not_seen_item_id_list_v2": None,
                "contrail_list": None,
                "data_label_list": None,
                "cover_url": [
                    {
                        "uri": "c8510002be9a3a61aad2",
                        "url_list": [
                            "https://p3-pc-sign.douyinpic.com/obj/c8510002be9a3a61aad2?lk3s=138a59ce&x-expires=1741683600&x-signature=EFWLy4VShefql8py2jCihCNLrr4%3D&from=327834062",
                            "https://p9-pc-sign.douyinpic.com/obj/c8510002be9a3a61aad2?lk3s=138a59ce&x-expires=1741683600&x-signature=jVI%2FKFrse7iVVzpzakMSFh%2BWQnU%3D&from=327834062"
                        ],
                        "width": 720,
                        "height": 720
                    }
                ],
                "user_permissions": None,
                "offline_info_list": None,
                "endorsement_info_list": None,
                "interest_tags": None,
                "personal_tag_list": None,
                "white_cover_url": None,
                "creator_tag_list": None,
                "special_people_labels": None
            },
            "music": {
                "id": 7356558561755105000,
                "id_str": "7356558561755105297",
                "title": "漫步香港1999",
                "author": "布鲁昔",
                "album": "漫步香港1999",
                "cover_hd": {
                    "uri": "tos-cn-v-2774c002/o8ADu7MRAvzeITdaL3FAtEEGXAdgLA3CDleS2f",
                    "url_list": [
                        "https://p3.douyinpic.com/aweme/1080x1080/tos-cn-v-2774c002/o8ADu7MRAvzeITdaL3FAtEEGXAdgLA3CDleS2f.jpeg",
                        "https://p11.douyinpic.com/aweme/1080x1080/tos-cn-v-2774c002/o8ADu7MRAvzeITdaL3FAtEEGXAdgLA3CDleS2f.jpeg"
                    ],
                    "width": 720,
                    "height": 720
                },
                "cover_large": {
                    "uri": "tos-cn-v-2774c002/o8ADu7MRAvzeITdaL3FAtEEGXAdgLA3CDleS2f",
                    "url_list": [
                        "https://p3.douyinpic.com/aweme/720x720/tos-cn-v-2774c002/o8ADu7MRAvzeITdaL3FAtEEGXAdgLA3CDleS2f.jpeg",
                        "https://p11.douyinpic.com/aweme/720x720/tos-cn-v-2774c002/o8ADu7MRAvzeITdaL3FAtEEGXAdgLA3CDleS2f.jpeg"
                    ],
                    "width": 720,
                    "height": 720
                },
                "cover_medium": {
                    "uri": "tos-cn-v-2774c002/o8ADu7MRAvzeITdaL3FAtEEGXAdgLA3CDleS2f",
                    "url_list": [
                        "https://p3.douyinpic.com/aweme/200x200/tos-cn-v-2774c002/o8ADu7MRAvzeITdaL3FAtEEGXAdgLA3CDleS2f.jpeg",
                        "https://p11.douyinpic.com/aweme/200x200/tos-cn-v-2774c002/o8ADu7MRAvzeITdaL3FAtEEGXAdgLA3CDleS2f.jpeg"
                    ],
                    "width": 720,
                    "height": 720
                },
                "cover_thumb": {
                    "uri": "tos-cn-v-2774c002/o8ADu7MRAvzeITdaL3FAtEEGXAdgLA3CDleS2f",
                    "url_list": [
                        "https://p3.douyinpic.com/aweme/100x100/tos-cn-v-2774c002/o8ADu7MRAvzeITdaL3FAtEEGXAdgLA3CDleS2f.jpeg",
                        "https://p11.douyinpic.com/aweme/100x100/tos-cn-v-2774c002/o8ADu7MRAvzeITdaL3FAtEEGXAdgLA3CDleS2f.jpeg"
                    ],
                    "width": 720,
                    "height": 720
                },
                "play_url": {
                    "uri": "https://sf5-hl-cdn-tos.douyinstatic.com/obj/tos-cn-ve-2774/osoi2vh2Ic2WoiCAtXzBvA9sfZBiQa9wDCdzMc",
                    "url_list": [
                        "https://sf5-hl-cdn-tos.douyinstatic.com/obj/tos-cn-ve-2774/osoi2vh2Ic2WoiCAtXzBvA9sfZBiQa9wDCdzMc",
                        "https://sf3-cdn-tos.douyinstatic.com/obj/tos-cn-ve-2774/osoi2vh2Ic2WoiCAtXzBvA9sfZBiQa9wDCdzMc"
                    ],
                    "width": 720,
                    "height": 720,
                    "url_key": "7356558561755105297"
                },
                "schema_url": "",
                "source_platform": 10036,
                "start_time": 0,
                "end_time": 0,
                "duration": 221,
                "extra": "{\"douyin_beats_info\":{},\"cover_colors\":{\"rgb\":[45,42,28]},\"peak\":\"1.1641449\",\"hit_high_follow_extend\":False,\"beats\":{\"audio_effect_onset\":\"https://sf3-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/ooEuEAAAZjpLCdzmYfA9tHqbQfBtjhAgCJo8B5\",\"beats_tracker\":\"https://sf6-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/o4rBAfMIdM9nlCOHAHa4RbDKeaFzBAXCfQg8AI\",\"energy_trace\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/ow0MXAneIBCDABDhbaFAIeA8SRdHiGJf4ZrzGH\",\"merged_beats\":\"https://sf3-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/oIfXnbIHaDvEI4H1nAMAeCYdIizRFAxmBBeAzm\"},\"is_subsidy_exp\":False,\"hit_high_follow_original\":False,\"hit_high_follow_auto\":False,\"reviewed\":1,\"review_unshelve_reason\":0,\"image_beats_url\":\"https://sf6-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/o4rBAfMIdM9nlCOHAHa4RbDKeaFzBAXCfQg8AI\",\"music_tagging\":{\"Languages\":[\"Chinese\",\"Cantonese\"],\"Moods\":[\"Romantic\",\"Happy\"],\"Genres\":[\"Chinese Pop\",\"Pop\",\"R&B/Soul\"],\"Themes\":[\"Sunny\"],\"AEDs\":[\"Male\",\"Vocal\"],\"SingingVersions\":[\"republished version\"],\"Instruments\":None},\"is_red\":0,\"is_aed_music\":0,\"has_edited\":0,\"schedule_search_time\":0,\"hotsoon_review_time\":-1,\"music_label_id\":1711,\"aggregate_exempt_conf\":[],\"with_aed_model\":0,\"loudness\":\"-9.310957\",\"is_high_follow_user\":False,\"dsp_switch\":0}",
                "user_count": 0,
                "position": None,
                "collect_stat": 0,
                "status": 1,
                "offline_desc": "",
                "owner_id": "57257252668",
                "owner_nickname": "",
                "is_original": True,
                "mid": "7356558561755105297",
                "binded_challenge_id": 0,
                "redirect": False,
                "is_restricted": False,
                "author_deleted": False,
                "is_del_video": False,
                "is_video_self_see": False,
                "owner_handle": "",
                "author_position": None,
                "prevent_download": False,
                "strong_beat_url": {
                    "uri": "https://sf5-hl-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/o8AAsjBliAGch1KYAs01BASWIyoEEhAfQzWyki",
                    "url_list": [
                        "https://sf5-hl-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/o8AAsjBliAGch1KYAs01BASWIyoEEhAfQzWyki",
                        "https://sf3-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/o8AAsjBliAGch1KYAs01BASWIyoEEhAfQzWyki"
                    ],
                    "width": 720,
                    "height": 720
                },
                "unshelve_countries": None,
                "prevent_item_download_status": 0,
                "external_song_info": [],
                "sec_uid": "MS4wLjABAAAA6Huf7c2S3sBMn7T1k79j91jABVAga6btfxpYVtY6Jtw",
                "avatar_thumb": {
                    "uri": "100x100/aweme-avatar/tos-cn-i-0813_oEs7zzABfACAAHBEAAU6YNIgEiemWvSA3CiEAN",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_oEs7zzABfACAAHBEAAU6YNIgEiemWvSA3CiEAN.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "avatar_medium": {
                    "uri": "720x720/aweme-avatar/tos-cn-i-0813_oEs7zzABfACAAHBEAAU6YNIgEiemWvSA3CiEAN",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-i-0813_oEs7zzABfACAAHBEAAU6YNIgEiemWvSA3CiEAN.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "avatar_large": {
                    "uri": "1080x1080/aweme-avatar/tos-cn-i-0813_oEs7zzABfACAAHBEAAU6YNIgEiemWvSA3CiEAN",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-i-0813_oEs7zzABfACAAHBEAAU6YNIgEiemWvSA3CiEAN.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "preview_start_time": 0,
                "preview_end_time": 0,
                "is_commerce_music": False,
                "is_original_sound": False,
                "audition_duration": 221,
                "shoot_duration": 221,
                "reason_type": 0,
                "artists": [
                    {
                        "uid": "57257252668",
                        "sec_uid": "MS4wLjABAAAA6Huf7c2S3sBMn7T1k79j91jABVAga6btfxpYVtY6Jtw",
                        "nick_name": "布鲁昔（做新专辑版）",
                        "handle": "",
                        "avatar": {
                            "uri": "168x168/aweme-avatar/tos-cn-i-0813_oEs7zzABfACAAHBEAAU6YNIgEiemWvSA3CiEAN",
                            "url_list": [
                                "https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-i-0813_oEs7zzABfACAAHBEAAU6YNIgEiemWvSA3CiEAN~c5_168x168.jpeg?from=327834062"
                            ]
                        },
                        "is_verified": False,
                        "enter_type": 1
                    }
                ],
                "lyric_short_position": None,
                "mute_share": False,
                "tag_list": None,
                "dmv_auto_show": False,
                "is_pgc": True,
                "is_matched_metadata": False,
                "is_audio_url_with_cookie": False,
                "music_chart_ranks": None,
                "can_background_play": True,
                "music_status": 1,
                "video_duration": 6000,
                "pgc_music_type": 1,
                "cover_color_hsv": {
                    "h": 49,
                    "s": 35,
                    "v": 18
                },
                "author_status": 1,
                "search_impr": {
                    "entity_id": "7356558561755105297"
                },
                "song": {
                    "id": 7356558376879835000,
                    "id_str": "7356558376879835153",
                    "title": "漫步香港1999",
                    "artists": None,
                    "chorus": {
                        "start_ms": 76416,
                        "duration_ms": 28800
                    },
                    "chorus_v3_infos": None
                },
                "artist_user_infos": None,
                "dsp_status": 10,
                "musician_user_infos": None,
                "music_image_beats": {
                    "music_image_beats_url": {
                        "uri": "tos-cn-v-2774c002/o4rBAfMIdM9nlCOHAHa4RbDKeaFzBAXCfQg8AI",
                        "url_list": [
                            "https://sf6-cdn-tos.douyinstatic.com/obj/tos-cn-v-2774c002/o4rBAfMIdM9nlCOHAHa4RbDKeaFzBAXCfQg8AI"
                        ],
                        "width": 720,
                        "height": 720
                    }
                },
                "music_collect_count": 0,
                "music_cover_atmosphere_color_value": ""
            }
        },
        {
            "aweme_id": "7401328596851117312",
            "desc": "好喜欢bgm女声出来的那秒哦～",
            "create_time": 1723256112,
            "author": {
                "uid": "3548856441386627",
                "ban_user_functions": None,
                "nickname": "小苏菲Yomi",
                "cf_list": None,
                "link_item_list": None,
                "avatar_thumb": {
                    "uri": "100x100/aweme-avatar/tos-cn-avt-0015_e586aa279259812ff17c84d58dcd7f7a",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_e586aa279259812ff17c84d58dcd7f7a.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "avatar_schema_list": None,
                "signature_extra": None,
                "follow_status": 0,
                "risk_notice_text": "",
                "private_relation_list": None,
                "follower_list_secondary_information_struct": None,
                "custom_verify": "",
                "can_set_geofencing": None,
                "batch_unfollow_contain_tabs": None,
                "display_info": None,
                "verification_permission_ids": None,
                "need_points": None,
                "share_info": {
                    "share_url": "",
                    "share_weibo_desc": "",
                    "share_desc": "",
                    "share_title": "",
                    "share_qrcode_url": {
                        "uri": "2e465000801715cb87430",
                        "url_list": [
                            "https://p3-pc-sign.douyinpic.com/obj/2e465000801715cb87430?lk3s=138a59ce&x-expires=1740495600&x-signature=VLET5Kqlj%2Bzz76z6PjTwcsQA7mM%3D&from=327834062",
                            "https://p9-pc-sign.douyinpic.com/obj/2e465000801715cb87430?lk3s=138a59ce&x-expires=1740495600&x-signature=G4rxLZLC8R9dqRfORvRhgI%2BkpW4%3D&from=327834062"
                        ],
                        "width": 720,
                        "height": 720
                    },
                    "share_title_myself": "",
                    "share_title_other": "",
                    "share_desc_info": ""
                },
                "familiar_visitor_user": None,
                "homepage_bottom_toast": None,
                "batch_unfollow_relation_desc": None,
                "enterprise_verify_reason": "",
                "is_ad_fake": False,
                "account_cert_info": "{}",
                "card_entries_not_display": None,
                "user_tags": None,
                "profile_mob_params": None,
                "card_sort_priority": None,
                "not_seen_item_id_list": None,
                "card_entries": None,
                "prevent_download": False,
                "text_extra": None,
                "sec_uid": "MS4wLjABAAAA0HwZJN6-JDCSTjxiMk-czhyZWxes8XIDEjppFXExauK8-kQTLMEH9ZdfIXxnl9tS",
                "im_role_ids": None,
                "follower_status": 0,
                "not_seen_item_id_list_v2": None,
                "contrail_list": None,
                "data_label_list": None,
                "cover_url": [
                    {
                        "uri": "c8510002be9a3a61aad2",
                        "url_list": [
                            "https://p3-pc-sign.douyinpic.com/obj/c8510002be9a3a61aad2?lk3s=138a59ce&x-expires=1741683600&x-signature=EFWLy4VShefql8py2jCihCNLrr4%3D&from=327834062",
                            "https://p9-pc-sign.douyinpic.com/obj/c8510002be9a3a61aad2?lk3s=138a59ce&x-expires=1741683600&x-signature=jVI%2FKFrse7iVVzpzakMSFh%2BWQnU%3D&from=327834062"
                        ],
                        "width": 720,
                        "height": 720
                    }
                ],
                "user_permissions": None,
                "offline_info_list": None,
                "endorsement_info_list": None,
                "interest_tags": None,
                "personal_tag_list": None,
                "white_cover_url": None,
                "creator_tag_list": None,
                "special_people_labels": None
            },
            "music": {
                "id": 7107553327847656000,
                "id_str": "7107553327847656206",
                "title": "@ouoao_创作的原声",
                "author": "ouoao_",
                "album": "",
                "cover_hd": {
                    "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "cover_large": {
                    "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "cover_medium": {
                    "uri": "720x720/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "cover_thumb": {
                    "uri": "100x100/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "play_url": {
                    "uri": "https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/7107553323397483277.mp3",
                    "url_list": [
                        "https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/7107553323397483277.mp3",
                        "https://sf6-cdn-tos.douyinstatic.com/obj/ies-music/7107553323397483277.mp3"
                    ],
                    "width": 720,
                    "height": 720,
                    "url_key": "7107553327847656206"
                },
                "schema_url": "",
                "source_platform": 23,
                "start_time": 0,
                "end_time": 0,
                "duration": 21,
                "extra": "{\"reviewed\":1,\"schedule_search_time\":0,\"music_tagging\":{\"Languages\":[\"Chinese\"],\"Moods\":[\"Memory\",\"Miss\"],\"Genres\":[\"Pop\",\"Chinese Pop\"],\"Themes\":[\"Love\",\"SoundTrack\"],\"AEDs\":[\"Vocal\",\"Female\"],\"SingingVersions\":[\"republished version\"],\"Instruments\":None},\"is_subsidy_exp\":False,\"dsp_switch\":0,\"has_edited\":0,\"douyin_beats_info\":{},\"music_label_id\":None,\"aggregate_exempt_conf\":[],\"with_aed_model\":1,\"uniqa_speech_score\":0.32,\"review_unshelve_reason\":0,\"image_beats_url\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1735988065738823\",\"beats\":{\"beats_tracker\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1735988065738823\",\"energy_trace\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1735988064546824\",\"merged_beats\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1735988065783821\",\"audio_effect_onset\":\"https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1735988064605198\"},\"cover_colors\":None,\"extract_item_id\":7107553283727723809,\"is_aed_music\":0,\"aed_music_score\":0.09,\"hotsoon_review_time\":-1,\"is_red\":0,\"aed_singing_score\":0.27,\"is_high_follow_user\":False,\"hit_high_follow_original\":False,\"hit_high_follow_extend\":False,\"hit_high_follow_auto\":False}",
                "user_count": 0,
                "position": None,
                "collect_stat": 0,
                "status": 1,
                "offline_desc": "",
                "owner_id": "3394925711071805",
                "owner_nickname": "ouoao_",
                "is_original": False,
                "mid": "7107553327847656206",
                "binded_challenge_id": 0,
                "redirect": False,
                "is_restricted": False,
                "author_deleted": False,
                "is_del_video": False,
                "is_video_self_see": False,
                "owner_handle": "38528167827",
                "author_position": None,
                "prevent_download": False,
                "strong_beat_url": {
                    "uri": "https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/pattern/4a260693a9eb3bfffd22d831d4695213.json",
                    "url_list": [
                        "https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/pattern/4a260693a9eb3bfffd22d831d4695213.json",
                        "https://sf6-cdn-tos.douyinstatic.com/obj/ies-music/pattern/4a260693a9eb3bfffd22d831d4695213.json"
                    ],
                    "width": 720,
                    "height": 720
                },
                "unshelve_countries": None,
                "prevent_item_download_status": 0,
                "external_song_info": [],
                "sec_uid": "MS4wLjABAAAAIBw6JrIoOr1Gvz4xFlknspTFyMWvZog5Fnc-fkRgys7LMjK3Gtuc9s0Uw3WUIiX3",
                "avatar_thumb": {
                    "uri": "100x100/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "avatar_medium": {
                    "uri": "720x720/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "avatar_large": {
                    "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_a90cdfdb9c5f9fb5128cb24213a9eaec.jpeg?from=327834062"
                    ],
                    "width": 720,
                    "height": 720
                },
                "preview_start_time": 0,
                "preview_end_time": 0,
                "is_commerce_music": False,
                "is_original_sound": True,
                "audition_duration": 21,
                "shoot_duration": 21,
                "reason_type": 0,
                "artists": [],
                "lyric_short_position": None,
                "mute_share": False,
                "tag_list": None,
                "dmv_auto_show": False,
                "is_pgc": False,
                "is_matched_metadata": False,
                "is_audio_url_with_cookie": False,
                "matched_pgc_sound": {
                    "author": "Enno Cheng",
                    "title": "第一次遇見花香的那刻 - 劇集《第一次遇見花香的那刻》主題曲",
                    "mixed_title": "",
                    "mixed_author": "",
                    "cover_medium": {
                        "uri": "tos-cn-v-2774c002/9c07ebdb2ef0491ea6eebd788c0591e4",
                        "url_list": [
                            "https://p3.douyinpic.com/aweme/200x200/tos-cn-v-2774c002/9c07ebdb2ef0491ea6eebd788c0591e4.jpeg",
                            "https://p26.douyinpic.com/aweme/200x200/tos-cn-v-2774c002/9c07ebdb2ef0491ea6eebd788c0591e4.jpeg",
                            "https://p11.douyinpic.com/aweme/200x200/tos-cn-v-2774c002/9c07ebdb2ef0491ea6eebd788c0591e4.jpeg"
                        ],
                        "width": 720,
                        "height": 720
                    }
                },
                "music_chart_ranks": None,
                "can_background_play": True,
                "music_status": 1,
                "video_duration": 21,
                "pgc_music_type": 2,
                "author_status": 1,
                "search_impr": {
                    "entity_id": "7107553327847656206"
                },
                "song": {
                    "id": 7023824296950630000,
                    "id_str": "7023824296950630401",
                    "artists": None,
                    "chorus_v3_infos": None
                },
                "artist_user_infos": None,
                "dsp_status": 10,
                "musician_user_infos": None,
                "music_image_beats": {
                    "music_image_beats_url": {
                        "uri": "ies-music/strong_beat/v3/1735988065738823",
                        "url_list": [
                            "https://sf5-hl-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1735988065738823"
                        ],
                        "width": 720,
                        "height": 720
                    }
                },
                "music_collect_count": 0,
                "music_cover_atmosphere_color_value": ""
            }
        }
    ]
}

aweme_list = data.get("aweme_list")

# 方法一：遍历
ret = []
for aweme in aweme_list:
    author = aweme.get("music").get("author")
    title = aweme.get("music").get("title")
    play_url = aweme.get("music").get("play_url").get("url_list")[0]
    ret.append((author, title, play_url))

print(ret)

# 方式2：列表推导式
ret = [(aweme.get("music").get("author"), aweme.get("music").get("title"), aweme.get("music").get("play_url").get("url_list")[0])
       for aweme in aweme_list]
print(ret)

# 课堂讲解
li = []
for aweme in data.get("aweme_list"):
    print("title:", aweme.get("music").get("title"))
    print("author:", aweme.get("music").get("author"))
    print("url:", aweme.get("music").get("play_url").get("url_list")[0])

    item = (aweme.get("music").get("title"), aweme.get("music").get("author"),
            aweme.get("music").get("play_url").get("url_list")[0])
    li.append(item)
