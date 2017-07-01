# -*- coding: utf-8 -*-

from plugins.common.BaseMessenger import BaseMessenger
from plugins.common.OutputLevelManager import OutputLevelManager

class OutputLevelMessenger(BaseMessenger):
    """メッセージ出力レベルに関するコマンドの管理クラス"""

    __OUTPUT_LEVEL = 0
    """
    自クラスのメッセージ出力レベル
    このクラスのみ例外的に0とし常に出力する
    """

    __SETLEVEL_USAGE = "Usage:setlevel 出力レベル"
    """setlevelコマンドのUsage"""

    __DISPLEVEL_USAGE = "Usage:displevel"
    """displevelコマンドのUsage"""

    __COMMAND_DISP = "displevel"
    """displevelコマンドの文字列"""

    setlevel = 10
    """コマンドで受け取った設定する出力レベル"""

    def __init__(self):
        """コンストラクタ"""
        self.set_message_level(self.__OUTPUT_LEVEL)

    def set_message_level(self, level):
        """
        メッセージの出力レベル設定
        param level:設定するメッセージ出力レベル
        """
        super().set_message_output_level(level)

    def exec_set(self, message):
        """
        出力レベル設定コマンド実行
        param message:受け取ったメッセージの文字列
        return:botが応答するメッセージ
        """
        errmsg = self.get_errmsg_about_arg(message)

        # エラーがある場合はエラーメッセージを返す
        if errmsg:
            return errmsg

        OutputLevelManager.set_output_level(self.setlevel)

        return "出力レベルを%dに設定しました" % (self.setlevel)

    def exec_disp(self, message):
        """
        出力レベル表示コマンド実行
        param message:受け取ったメッセージの文字列
        return:botが応答するメッセージ
        """

        if not self.__COMMAND_DISP == message:
            return "コマンドが不正です\n" + self.__SETLEVEL_USAGE

        level = OutputLevelManager.get_output_level()
        return "現在の出力レベルは%dです" % (level)

    def get_errmsg_about_arg(self, msg):
        """
        入力コマンドチェック処理
        param msg:受け取ったメッセージの文字列
        return:エラーありの場合はエラーメッセージ
               エラーなしの場合は空文字
        """
        super().check_output_level()

        args = msg.split()

        if len(args) == 1:
             return "出力レベルが未入力です\n" + self.__SETLEVEL_USAGE
        elif len(args) > 2:
             return "コマンドが不正です\n" + self.__SETLEVEL_USAGE

        if not args[1].isdigit():
            return "出力レベルは0〜10の数字を指定してください\n" + self.__SETLEVEL_USAGE

        level = int(args[1])

        if level < 0 or level > 10:
            return "出力レベルは0〜10の数字を指定してください\n" + self.__SETLEVEL_USAGE

        self.setlevel = level
        return ""
