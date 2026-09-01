// Instant Fast Search for FTMGram Docs
const FTM_SEARCH_INDEX = [{"name": "Rich Messages (Bot API 10.3)", "cat": "Bot API 10.3", "url": "topics/rich-messages.html"}, {"name": "In-Message Buttons (<tg-button-row>)", "cat": "Bot API 10.3", "url": "topics/intext-buttons.html"}, {"name": "AI Response Streaming & Drafts", "cat": "Bot API 10.3", "url": "topics/streaming-drafts.html"}, {"name": "Ephemeral Messages & Overlays", "cat": "Bot API 10.3", "url": "topics/ephemeral.html"}, {"name": "Checklists & Task Lists", "cat": "Bot API 10.3", "url": "topics/checklists.html"}, {"name": "Quick Start", "cat": "Guide", "url": "intro/quickstart.html"}, {"name": "Installation", "cat": "Guide", "url": "intro/install.html"}, {"name": "Client Methods Index", "cat": "API Reference", "url": "api/methods/index.html"}, {"name": "Types Index", "cat": "API Reference", "url": "api/types/index.html"}, {"name": "Enums Index", "cat": "API Reference", "url": "api/enums/index.html"}, {"name": "Bound Methods Index", "cat": "API Reference", "url": "api/bound-methods/index.html"}, {"name": "Smart Plugins", "cat": "Topics", "url": "topics/smart-plugins.html"}, {"name": "Storage Engines", "cat": "Topics", "url": "topics/storage-engines.html"}, {"name": "Text Formatting", "cat": "Topics", "url": "topics/text-formatting.html"}, {"name": "send_message", "cat": "Methods (Messages)", "url": "api/methods/send_message.html"}, {"name": "send_rich_message", "cat": "Methods (Messages)", "url": "api/methods/send_rich_message.html"}, {"name": "send_rich_message_draft", "cat": "Methods (Messages)", "url": "api/methods/send_rich_message_draft.html"}, {"name": "send_message_draft", "cat": "Methods (Messages)", "url": "api/methods/send_message_draft.html"}, {"name": "send_photo", "cat": "Methods (Messages)", "url": "api/methods/send_photo.html"}, {"name": "send_audio", "cat": "Methods (Messages)", "url": "api/methods/send_audio.html"}, {"name": "send_video", "cat": "Methods (Messages)", "url": "api/methods/send_video.html"}, {"name": "send_document", "cat": "Methods (Messages)", "url": "api/methods/send_document.html"}, {"name": "send_animation", "cat": "Methods (Messages)", "url": "api/methods/send_animation.html"}, {"name": "send_sticker", "cat": "Methods (Messages)", "url": "api/methods/send_sticker.html"}, {"name": "send_voice", "cat": "Methods (Messages)", "url": "api/methods/send_voice.html"}, {"name": "send_video_note", "cat": "Methods (Messages)", "url": "api/methods/send_video_note.html"}, {"name": "send_location", "cat": "Methods (Messages)", "url": "api/methods/send_location.html"}, {"name": "send_contact", "cat": "Methods (Messages)", "url": "api/methods/send_contact.html"}, {"name": "send_poll", "cat": "Methods (Messages)", "url": "api/methods/send_poll.html"}, {"name": "send_dice", "cat": "Methods (Messages)", "url": "api/methods/send_dice.html"}, {"name": "send_media_group", "cat": "Methods (Messages)", "url": "api/methods/send_media_group.html"}, {"name": "send_checklist", "cat": "Methods (Messages)", "url": "api/methods/send_checklist.html"}, {"name": "forward_messages", "cat": "Methods (Messages)", "url": "api/methods/forward_messages.html"}, {"name": "copy_message", "cat": "Methods (Messages)", "url": "api/methods/copy_message.html"}, {"name": "edit_message_text", "cat": "Methods (Messages)", "url": "api/methods/edit_message_text.html"}, {"name": "edit_message_caption", "cat": "Methods (Messages)", "url": "api/methods/edit_message_caption.html"}, {"name": "edit_message_media", "cat": "Methods (Messages)", "url": "api/methods/edit_message_media.html"}, {"name": "edit_message_reply_markup", "cat": "Methods (Messages)", "url": "api/methods/edit_message_reply_markup.html"}, {"name": "edit_ephemeral_message_text", "cat": "Methods (Messages)", "url": "api/methods/edit_ephemeral_message_text.html"}, {"name": "delete_ephemeral_message", "cat": "Methods (Messages)", "url": "api/methods/delete_ephemeral_message.html"}, {"name": "delete_messages", "cat": "Methods (Messages)", "url": "api/methods/delete_messages.html"}, {"name": "get_messages", "cat": "Methods (Messages)", "url": "api/methods/get_messages.html"}, {"name": "get_chat_history", "cat": "Methods (Messages)", "url": "api/methods/get_chat_history.html"}, {"name": "search_messages", "cat": "Methods (Messages)", "url": "api/methods/search_messages.html"}, {"name": "download_media", "cat": "Methods (Messages)", "url": "api/methods/download_media.html"}, {"name": "send_chat_action", "cat": "Methods (Messages)", "url": "api/methods/send_chat_action.html"}, {"name": "get_chat", "cat": "Methods (Chats)", "url": "api/methods/get_chat.html"}, {"name": "get_dialogs", "cat": "Methods (Chats)", "url": "api/methods/get_dialogs.html"}, {"name": "join_chat", "cat": "Methods (Chats)", "url": "api/methods/join_chat.html"}, {"name": "leave_chat", "cat": "Methods (Chats)", "url": "api/methods/leave_chat.html"}, {"name": "create_group", "cat": "Methods (Chats)", "url": "api/methods/create_group.html"}, {"name": "create_channel", "cat": "Methods (Chats)", "url": "api/methods/create_channel.html"}, {"name": "create_supergroup", "cat": "Methods (Chats)", "url": "api/methods/create_supergroup.html"}, {"name": "get_chat_members", "cat": "Methods (Chats)", "url": "api/methods/get_chat_members.html"}, {"name": "get_chat_member", "cat": "Methods (Chats)", "url": "api/methods/get_chat_member.html"}, {"name": "ban_chat_member", "cat": "Methods (Chats)", "url": "api/methods/ban_chat_member.html"}, {"name": "unban_chat_member", "cat": "Methods (Chats)", "url": "api/methods/unban_chat_member.html"}, {"name": "restrict_chat_member", "cat": "Methods (Chats)", "url": "api/methods/restrict_chat_member.html"}, {"name": "promote_chat_member", "cat": "Methods (Chats)", "url": "api/methods/promote_chat_member.html"}, {"name": "set_chat_title", "cat": "Methods (Chats)", "url": "api/methods/set_chat_title.html"}, {"name": "set_chat_description", "cat": "Methods (Chats)", "url": "api/methods/set_chat_description.html"}, {"name": "pin_chat_message", "cat": "Methods (Chats)", "url": "api/methods/pin_chat_message.html"}, {"name": "unpin_chat_message", "cat": "Methods (Chats)", "url": "api/methods/unpin_chat_message.html"}, {"name": "get_me", "cat": "Methods (Users)", "url": "api/methods/get_me.html"}, {"name": "get_users", "cat": "Methods (Users)", "url": "api/methods/get_users.html"}, {"name": "block_user", "cat": "Methods (Users)", "url": "api/methods/block_user.html"}, {"name": "unblock_user", "cat": "Methods (Users)", "url": "api/methods/unblock_user.html"}, {"name": "update_profile", "cat": "Methods (Users)", "url": "api/methods/update_profile.html"}, {"name": "answer_callback_query", "cat": "Methods (Bots)", "url": "api/methods/answer_callback_query.html"}, {"name": "answer_inline_query", "cat": "Methods (Bots)", "url": "api/methods/answer_inline_query.html"}, {"name": "set_bot_commands", "cat": "Methods (Bots)", "url": "api/methods/set_bot_commands.html"}, {"name": "get_bot_commands", "cat": "Methods (Bots)", "url": "api/methods/get_bot_commands.html"}, {"name": "delete_bot_commands", "cat": "Methods (Bots)", "url": "api/methods/delete_bot_commands.html"}, {"name": "answer_chat_join_request_query", "cat": "Methods (Bots)", "url": "api/methods/answer_chat_join_request_query.html"}, {"name": "send_chat_join_request_web_app", "cat": "Methods (Bots)", "url": "api/methods/send_chat_join_request_web_app.html"}, {"name": "get_owned_star_count", "cat": "Methods (Stars)", "url": "api/methods/get_owned_star_count.html"}, {"name": "send_invoice", "cat": "Methods (Stars)", "url": "api/methods/send_invoice.html"}, {"name": "refund_star_payment", "cat": "Methods (Stars)", "url": "api/methods/refund_star_payment.html"}, {"name": "Message", "cat": "Types", "url": "api/types/Message.html"}, {"name": "Chat", "cat": "Types", "url": "api/types/Chat.html"}, {"name": "User", "cat": "Types", "url": "api/types/User.html"}, {"name": "InputRichMessage", "cat": "Types (Bot API 10.3)", "url": "api/types/InputRichMessage.html"}, {"name": "InputRichBlockButtons", "cat": "Types (Bot API 10.3)", "url": "api/types/InputRichBlockButtons.html"}, {"name": "RichMessageButton", "cat": "Types (Bot API 10.3)", "url": "api/types/RichMessageButton.html"}, {"name": "InputRichBlockParagraph", "cat": "Types (Bot API 10.3)", "url": "api/types/InputRichBlockParagraph.html"}, {"name": "InputRichBlockTable", "cat": "Types (Bot API 10.3)", "url": "api/types/InputRichBlockTable.html"}, {"name": "InputRichBlockExpandableBlockQuotation", "cat": "Types (Bot API 10.3)", "url": "api/types/InputRichBlockExpandableBlockQuotation.html"}, {"name": "EphemeralMessageParameters", "cat": "Types (Bot API 10.3)", "url": "api/types/EphemeralMessageParameters.html"}, {"name": "DisabledButton", "cat": "Types (Bot API 10.3)", "url": "api/types/DisabledButton.html"}, {"name": "Community", "cat": "Types (Bot API 10.3)", "url": "api/types/Community.html"}, {"name": "Checklist", "cat": "Types", "url": "api/types/Checklist.html"}, {"name": "ChecklistTask", "cat": "Types", "url": "api/types/ChecklistTask.html"}, {"name": "Link", "cat": "Types", "url": "api/types/Link.html"}, {"name": "InlineKeyboardMarkup", "cat": "Types", "url": "api/types/InlineKeyboardMarkup.html"}, {"name": "InlineKeyboardButton", "cat": "Types", "url": "api/types/InlineKeyboardButton.html"}, {"name": "CallbackQuery", "cat": "Types", "url": "api/types/CallbackQuery.html"}, {"name": "InlineQuery", "cat": "Types", "url": "api/types/InlineQuery.html"}, {"name": "ChatType", "cat": "Enums", "url": "api/enums/ChatType.html"}, {"name": "ParseMode", "cat": "Enums", "url": "api/enums/ParseMode.html"}, {"name": "ButtonStyle", "cat": "Enums (Bot API 10.3)", "url": "api/enums/ButtonStyle.html"}, {"name": "MessageMediaType", "cat": "Enums", "url": "api/enums/MessageMediaType.html"}, {"name": "ChatMemberStatus", "cat": "Enums", "url": "api/enums/ChatMemberStatus.html"}, {"name": "ChatAction", "cat": "Enums", "url": "api/enums/ChatAction.html"}, {"name": "PollType", "cat": "Enums", "url": "api/enums/PollType.html"}, {"name": "UserStatus", "cat": "Enums", "url": "api/enums/UserStatus.html"}, {"name": "Message.reply", "cat": "Bound Methods", "url": "api/bound-methods/Message.reply.html"}, {"name": "Message.edit_text", "cat": "Bound Methods", "url": "api/bound-methods/Message.edit_text.html"}, {"name": "Message.delete", "cat": "Bound Methods", "url": "api/bound-methods/Message.delete.html"}, {"name": "Message.click", "cat": "Bound Methods", "url": "api/bound-methods/Message.click.html"}, {"name": "CallbackQuery.answer", "cat": "Bound Methods", "url": "api/bound-methods/CallbackQuery.answer.html"}, {"name": "Chat.ban_member", "cat": "Bound Methods", "url": "api/bound-methods/Chat.ban_member.html"}, {"name": "User.block", "cat": "Bound Methods", "url": "api/bound-methods/User.block.html"}, {"name": "MessageHandler (@app.on_message)", "cat": "Handlers", "url": "api/handlers.html"}, {"name": "CallbackQueryHandler", "cat": "Handlers", "url": "api/handlers.html"}, {"name": "InlineQueryHandler", "cat": "Handlers", "url": "api/handlers.html"}, {"name": "filters.text", "cat": "Filters", "url": "api/filters.html"}, {"name": "filters.command", "cat": "Filters", "url": "api/filters.html"}, {"name": "filters.private", "cat": "Filters", "url": "api/filters.html"}, {"name": "filters.group", "cat": "Filters", "url": "api/filters.html"}, {"name": "filters.regex", "cat": "Filters", "url": "api/filters.html"}, {"name": "filters.create", "cat": "Filters", "url": "api/filters.html"}];

(function() {
  document.addEventListener('DOMContentLoaded', () => {
    const searchInputs = document.querySelectorAll('input[name="q"], input.sidebar-search');
    
    const searchModal = document.createElement('div');
    searchModal.id = 'ftm-search-modal';
    searchModal.className = 'ftm-search-dropdown';
    document.body.appendChild(searchModal);

    function getDocRoot() {
      const loc = window.location.pathname;
      if (loc.includes('/api/methods/') || loc.includes('/api/types/') || loc.includes('/api/enums/') || loc.includes('/api/bound-methods/') || loc.includes('/start/examples/')) {
        return '../../';
      } else if (loc.includes('/api/') || loc.includes('/topics/') || loc.includes('/intro/') || loc.includes('/start/') || loc.includes('/faq/') || loc.includes('/releases/')) {
        return '../';
      }
      return './';
    }

    function renderResults(query, inputEl) {
      if (!query || query.trim().length === 0) {
        searchModal.style.display = 'none';
        return;
      }
      
      const q = query.toLowerCase().trim();
      const matches = FTM_SEARCH_INDEX.filter(item => 
        item.name.toLowerCase().includes(q) || item.cat.toLowerCase().includes(q)
      ).slice(0, 10);

      if (matches.length === 0) {
        searchModal.innerHTML = '<div class="ftm-search-empty">No results found for "<b>' + query + '</b>"</div>';
      } else {
        const root = getDocRoot();
        searchModal.innerHTML = matches.map(m => 
          '<a class="ftm-search-row" href="' + root + m.url + '">' +
            '<span class="ftm-search-name">' + m.name + '</span>' +
            '<span class="ftm-search-cat">' + m.cat + '</span>' +
          '</a>'
        ).join('');
      }

      const rect = inputEl.getBoundingClientRect();
      searchModal.style.top = (rect.bottom + window.scrollY + 6) + 'px';
      searchModal.style.left = (rect.left + window.scrollX) + 'px';
      searchModal.style.width = Math.max(rect.width, 320) + 'px';
      searchModal.style.display = 'block';
    }

    searchInputs.forEach(input => {
      input.setAttribute('autocomplete', 'off');
      input.setAttribute('placeholder', 'Instant Search (Ctrl + K)...');
      
      input.addEventListener('input', (e) => {
        renderResults(e.target.value, input);
      });

      input.addEventListener('focus', (e) => {
        if (e.target.value) renderResults(e.target.value, input);
      });
    });

    document.addEventListener('click', (e) => {
      if (!e.target.closest('#ftm-search-modal') && !e.target.closest('input[name="q"]')) {
        searchModal.style.display = 'none';
      }
    });

    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const firstInput = document.querySelector('input[name="q"]');
        if (firstInput) {
          firstInput.focus();
          firstInput.select();
        }
      } else if (e.key === 'Escape') {
        searchModal.style.display = 'none';
      }
    });
  });
})();
