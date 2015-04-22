# -*- coding: utf-8 -*-
from gi.repository import Gtk
import application
def retweet_question(parent):
 dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, _(u"Retweet"))
 dialog.format_secondary_text(_(u"Would you like to add a comment to this tweet?"))
 answer = dialog.run()
 dialog.destroy()
 return answer

def delete_tweet_dialog(parent):
 dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, _(u"Delete"))
 dialog.format_secondary_text(_(u"Do you really want to delete this message? It will be eliminated from Twitter as well."))
 answer = dialog.run()
 dialog.destroy()
 return answer

def exit_dialog(parent):
 dialog = Gtk.MessageDialog(parent, 0, Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, _(u"Exit"))
 dialog.format_secondary_text(_(u"Do you really want to close " + application.name + "?"))
 answer = dialog.run()
 dialog.destroy()
 return answer

def needs_restart():
 wx.MessageDialog(None, _(unicode(application.name+" must be restarted to save these changes. Press OK to restart now.")), _("Restart " + application.name), wx.OK).ShowModal()

def delete_user_from_db():
 return wx.MessageDialog(None, _(u"Are you sure you want to delete this user from the database? This user will not appear on the autocomplete results anymore."), _(u"Confirm"), wx.YES_NO|wx.ICON_QUESTION).ShowModal()

def get_ignored_client():
 entry = wx.TextEntryDialog(None, _(u"Enter the name of the client here"), _(u"Add a new ignored client"))
 if entry.ShowModal() == wx.ID_OK:
  return entry.GetValue()
 return None

def clear_list():
 dlg = wx.MessageDialog(None, _(u"Do you really want to empty this buffer? It's  items will be removed from the list but not from Twitter"), _(u"Empty buffer"), wx.ICON_QUESTION|wx.YES_NO)
 return dlg.ShowModal()

def remove_buffer():
 return wx.MessageDialog(None, _(u"Do you really want to delete this timeline?"), _(u"Attention"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def user_not_exist():
 return wx.MessageDialog(None, _(u"The user does not exist"), _(u"Error"), wx.ICON_ERROR).ShowModal()

def timeline_exist():
 return wx.MessageDialog(None, _(u"There's currently a timeline for this user. You are not able to open another"), _(u"Existing timeline"), wx.ICON_ERROR).ShowModal()

def no_tweets():
 return wx.MessageDialog(None, _(u"This user has no tweets. You can't open a timeline for this user"), _(u"Error!"), wx.ICON_ERROR).ShowModal()

def protected_user():
 return wx.MessageDialog(None, _(u"This is a protected Twitter user. It means you can not open a timeline using the Streaming API. The user's tweets will not update due to a twitter policy. Do you want to continue?"), _(u"Warning"), wx.ICON_WARNING|wx.YES_NO).ShowModal()

def no_following():
 return wx.MessageDialog(None, _(u"This is a protected user account, you need follow to this user for viewing your tweets or favourites."), _(u"Error"), wx.ICON_ERROR).ShowModal()