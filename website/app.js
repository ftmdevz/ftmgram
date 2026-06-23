/* ============================================================
   FTMGram Docs — app.js
   ============================================================ */

// ── Theme ────────────────────────────────────────────────────
(function () {
  const saved = localStorage.getItem('ftm-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
})();

function toggleTheme() {
  const cur = document.documentElement.getAttribute('data-theme');
  const next = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('ftm-theme', next);
}

// ── Sidebar ──────────────────────────────────────────────────
function toggleSidebar() {
  document.getElementById('sidebar').classList.toggle('open');
  document.getElementById('overlay').classList.toggle('open');
}
function closeSidebar() {
  document.getElementById('sidebar').classList.remove('open');
  document.getElementById('overlay').classList.remove('open');
}

// ── Section collapse ─────────────────────────────────────────
function toggleSection(el) {
  el.classList.toggle('collapsed');
  const children = el.nextElementSibling;
  if (children) {
    if (el.classList.contains('collapsed')) {
      children.style.maxHeight = '0';
    } else {
      children.style.maxHeight = children.scrollHeight + 'px';
    }
  }
}
// Set initial maxHeight for all open sections
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.sidebar-children').forEach(c => {
    c.style.maxHeight = c.scrollHeight + 'px';
  });
  // Start on home
  navigate(location.hash.replace('#', '') || 'home');
  // Highlight.js
  hljs.highlightAll();
});

// ── Copy button ───────────────────────────────────────────────
function copyCode(btn) {
  const code = btn.closest('.code-wrap').querySelector('code');
  navigator.clipboard.writeText(code.innerText).then(() => {
    btn.classList.add('copied');
    btn.innerHTML = '✓ Copied';
    setTimeout(() => {
      btn.classList.remove('copied');
      btn.innerHTML = '⎘ Copy';
    }, 2000);
  });
}

// ── Search ────────────────────────────────────────────────────
const SEARCH_INDEX = [
  // Getting Started
  { name: 'Home', cat: 'Home', page: 'home' },
  { name: 'Installation', cat: 'Getting Started', page: 'install' },
  { name: 'Quick Start', cat: 'Getting Started', page: 'quickstart' },
  { name: 'Client', cat: 'Getting Started', page: 'client' },
  // Messages
  { name: 'send_message', cat: 'Messages', page: 'send_message' },
  { name: 'send_photo', cat: 'Messages', page: 'send_photo' },
  { name: 'send_audio', cat: 'Messages', page: 'send_audio' },
  { name: 'send_video', cat: 'Messages', page: 'send_video' },
  { name: 'send_document', cat: 'Messages', page: 'send_document' },
  { name: 'send_animation', cat: 'Messages', page: 'send_animation' },
  { name: 'send_sticker', cat: 'Messages', page: 'send_sticker' },
  { name: 'send_voice', cat: 'Messages', page: 'send_voice' },
  { name: 'send_video_note', cat: 'Messages', page: 'send_video_note' },
  { name: 'send_location', cat: 'Messages', page: 'send_location' },
  { name: 'send_contact', cat: 'Messages', page: 'send_contact' },
  { name: 'send_poll', cat: 'Messages', page: 'send_poll' },
  { name: 'send_dice', cat: 'Messages', page: 'send_dice' },
  { name: 'send_media_group', cat: 'Messages', page: 'send_media_group' },
  { name: 'send_rich_message', cat: 'Messages', page: 'send_rich_message' },
  { name: 'send_checklist', cat: 'Messages', page: 'send_checklist' },
  { name: 'forward_message', cat: 'Messages', page: 'forward_message' },
  { name: 'copy_message', cat: 'Messages', page: 'copy_message' },
  { name: 'edit_message_text', cat: 'Messages', page: 'edit_message_text' },
  { name: 'delete_message', cat: 'Messages', page: 'delete_message' },
  { name: 'get_messages', cat: 'Messages', page: 'get_messages' },
  { name: 'get_chat_history', cat: 'Messages', page: 'get_chat_history' },
  { name: 'search_messages', cat: 'Messages', page: 'search_messages' },
  { name: 'download_media', cat: 'Messages', page: 'download_media' },
  { name: 'send_chat_action', cat: 'Messages', page: 'send_chat_action' },
  { name: 'translate_message_text', cat: 'Messages', page: 'translate_message_text' },
  // Chats
  { name: 'get_chat', cat: 'Chats', page: 'get_chat' },
  { name: 'get_dialogs', cat: 'Chats', page: 'get_dialogs' },
  { name: 'join_chat', cat: 'Chats', page: 'join_chat' },
  { name: 'leave_chat', cat: 'Chats', page: 'leave_chat' },
  { name: 'create_group', cat: 'Chats', page: 'create_group' },
  { name: 'create_channel', cat: 'Chats', page: 'create_channel' },
  { name: 'get_chat_members', cat: 'Chats', page: 'get_chat_members' },
  { name: 'ban_chat_member', cat: 'Chats', page: 'ban_chat_member' },
  { name: 'promote_chat_member', cat: 'Chats', page: 'promote_chat_member' },
  { name: 'set_chat_title', cat: 'Chats', page: 'set_chat_title' },
  { name: 'pin_chat_message', cat: 'Chats', page: 'pin_chat_message' },
  { name: 'get_chat_event_log', cat: 'Chats', page: 'get_chat_event_log' },
  // Users
  { name: 'get_me', cat: 'Users', page: 'get_me' },
  { name: 'get_users', cat: 'Users', page: 'get_users' },
  { name: 'get_user_profile_photos', cat: 'Users', page: 'get_user_profile_photos' },
  { name: 'block_user', cat: 'Users', page: 'block_user' },
  { name: 'unblock_user', cat: 'Users', page: 'unblock_user' },
  { name: 'update_profile', cat: 'Users', page: 'update_profile' },
  { name: 'set_profile_photo', cat: 'Users', page: 'set_profile_photo' },
  // Bots
  { name: 'answer_callback_query', cat: 'Bots', page: 'answer_callback_query' },
  { name: 'answer_inline_query', cat: 'Bots', page: 'answer_inline_query' },
  { name: 'set_bot_commands', cat: 'Bots', page: 'set_bot_commands' },
  { name: 'get_bot_commands', cat: 'Bots', page: 'get_bot_commands' },
  { name: 'send_invoice', cat: 'Bots', page: 'send_invoice' },
  { name: 'answer_pre_checkout_query', cat: 'Bots', page: 'answer_pre_checkout_query' },
  { name: 'answer_chat_join_request_query', cat: 'Bots', page: 'answer_chat_join_request_query' },
  { name: 'verify_user', cat: 'Bots', page: 'verify_user' },
  { name: 'create_bot', cat: 'Bots', page: 'create_bot' },
  // Utilities
  { name: 'start', cat: 'Utilities', page: 'start' },
  { name: 'stop', cat: 'Utilities', page: 'stop' },
  { name: 'run', cat: 'Utilities', page: 'run' },
  { name: 'idle', cat: 'Utilities', page: 'idle' },
  { name: 'add_handler', cat: 'Utilities', page: 'add_handler' },
  { name: 'export_session_string', cat: 'Utilities', page: 'export_session_string' },
  // Handlers
  { name: 'MessageHandler', cat: 'Handlers', page: 'message_handler' },
  { name: 'CallbackQueryHandler', cat: 'Handlers', page: 'callback_query_handler' },
  { name: 'InlineQueryHandler', cat: 'Handlers', page: 'inline_query_handler' },
  { name: 'EditedMessageHandler', cat: 'Handlers', page: 'edited_message_handler' },
  { name: 'ChatMemberUpdatedHandler', cat: 'Handlers', page: 'chat_member_updated_handler' },
  { name: 'ChatJoinRequestHandler', cat: 'Handlers', page: 'chat_join_request_handler' },
  { name: 'PollHandler', cat: 'Handlers', page: 'poll_handler' },
  { name: 'StoryHandler', cat: 'Handlers', page: 'story_handler' },
  { name: 'ErrorHandler', cat: 'Handlers', page: 'error_handler' },
  { name: 'RawUpdateHandler', cat: 'Handlers', page: 'raw_update_handler' },
  // Enums
  { name: 'ChatType', cat: 'Enums', page: 'enum_ChatType' },
  { name: 'ParseMode', cat: 'Enums', page: 'enum_ParseMode' },
  { name: 'MessageMediaType', cat: 'Enums', page: 'enum_MessageMediaType' },
  { name: 'ChatMemberStatus', cat: 'Enums', page: 'enum_ChatMemberStatus' },
  { name: 'ChatAction', cat: 'Enums', page: 'enum_ChatAction' },
  { name: 'MessageEntityType', cat: 'Enums', page: 'enum_MessageEntityType' },
  { name: 'SentCodeType', cat: 'Enums', page: 'enum_SentCodeType' },
  { name: 'MessagesFilter', cat: 'Enums', page: 'enum_MessagesFilter' },
  { name: 'ChatMembersFilter', cat: 'Enums', page: 'enum_ChatMembersFilter' },
  { name: 'StickerType', cat: 'Enums', page: 'enum_StickerType' },
  { name: 'ButtonStyle', cat: 'Enums', page: 'enum_ButtonStyle' },
  { name: 'ChatJoinType', cat: 'Enums', page: 'enum_ChatJoinType' },
  { name: 'GiftType', cat: 'Enums', page: 'enum_GiftType' },
  { name: 'PollType', cat: 'Enums', page: 'enum_PollType' },
  { name: 'UserStatus', cat: 'Enums', page: 'enum_UserStatus' },
  { name: 'BlockList', cat: 'Enums', page: 'enum_BlockList' },
  { name: 'ChatEventAction', cat: 'Enums', page: 'enum_ChatEventAction' },
  { name: 'FolderColor', cat: 'Enums', page: 'enum_FolderColor' },
  { name: 'MediaAreaType', cat: 'Enums', page: 'enum_MediaAreaType' },
  { name: 'PrivacyKey', cat: 'Enums', page: 'enum_PrivacyKey' },
];

function handleSearch(q) {
  const dd = document.getElementById('searchDropdown');
  if (!q.trim()) { dd.classList.remove('open'); dd.innerHTML = ''; return; }
  const results = SEARCH_INDEX.filter(i =>
    i.name.toLowerCase().includes(q.toLowerCase()) ||
    i.cat.toLowerCase().includes(q.toLowerCase())
  ).slice(0, 12);
  if (!results.length) {
    dd.innerHTML = '<div class="search-item"><span class="s-name" style="color:var(--text3)">No results found</span></div>';
  } else {
    dd.innerHTML = results.map(r =>
      `<div class="search-item" onmousedown="navigate('${r.page}')">
        <span class="s-name">${r.name}</span>
        <span class="s-cat">${r.cat}</span>
      </div>`
    ).join('');
  }
  dd.classList.add('open');
}
function showSearchDropdown() {
  const q = document.getElementById('searchInput').value;
  if (q.trim()) handleSearch(q);
}
function hideSearchDropdown() {
  setTimeout(() => document.getElementById('searchDropdown').classList.remove('open'), 150);
}

// ── Navigation ────────────────────────────────────────────────
let currentPage = '';
function navigate(page) {
  if (!page) page = 'home';
  currentPage = page;
  location.hash = page;
  closeSidebar();

  // Update active sidebar link
  document.querySelectorAll('.sidebar-link').forEach(l => l.classList.remove('active'));
  document.querySelectorAll('.sidebar-link').forEach(l => {
    if (l.getAttribute('onclick') && l.getAttribute('onclick').includes(`'${page}'`)) {
      l.classList.add('active');
    }
  });

  // Render page
  const content = document.getElementById('content');
  const renderer = PAGES[page];
  if (renderer) {
    content.innerHTML = renderer();
    window.scrollTo(0, 0);
    content.querySelectorAll('pre code').forEach(b => hljs.highlightElement(b));
  } else {
    content.innerHTML = `<div class="method-header"><h1>Page not found</h1><p>The page <code>${page}</code> does not exist.</p></div>`;
  }
}

// ── Helper builders ───────────────────────────────────────────
function codeBlock(lang, code) {
  return `<div class="code-wrap">
    <div class="code-header"><span class="code-lang">${lang}</span><button class="copy-btn" onclick="copyCode(this)">⎘ Copy</button></div>
    <pre><code class="language-${lang}">${escHtml(code.trim())}</code></pre>
  </div>`;
}
function escHtml(s) {
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}
function breadcrumb(cat, name) {
  return `<div class="breadcrumb"><a onclick="navigate('home')">Docs</a><span>/</span><span>${cat}</span>${name ? `<span>/</span><span>${name}</span>` : ''}</div>`;
}
function methodHeader(name, desc, tags) {
  const tagHtml = tags.map(t => {
    if (t==='users') return `<span class="tag tag-user">👤 Users</span>`;
    if (t==='bots') return `<span class="tag tag-bot">🤖 Bots</span>`;
    if (t==='new') return `<span class="tag tag-new">✨ New in v3</span>`;
    if (t==='async') return `<span class="tag tag-async">⚡ async</span>`;
    return '';
  }).join('');
  return `<div class="method-header">
    <h1><code style="font-size:1.4rem">${name}</code></h1>
    <p>${desc}</p>
    <div class="method-tags">${tagHtml}</div>
  </div>`;
}
function paramsTable(params) {
  const rows = params.map(p => `<tr>
    <td><span class="param-name">${p.name}</span><br><span class="param-opt">${p.required ? 'required' : 'optional'}</span></td>
    <td><span class="param-type">${escHtml(p.type)}</span></td>
    <td class="param-desc">${p.desc}</td>
  </tr>`).join('');
  return `<table class="params-table">
    <thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead>
    <tbody>${rows}</tbody>
  </table>`;
}
function returns(type, desc) {
  return `<div class="returns-box"><div><strong>Returns:</strong> <code>${type}</code> — ${desc}</div></div>`;
}
function enumPage(name, cat, desc, values) {
  const rows = values.map(v => `<div class="enum-row">
    <span class="enum-key">${name}.${v.key}</span>
    <span class="enum-val">${v.desc}</span>
  </div>`).join('');
  return `${breadcrumb(cat, name)}
  <div class="method-header">
    <h1>${name}</h1>
    <p>${desc}</p>
    <div class="method-tags"><span class="tag tag-async">🔷 Enum</span></div>
  </div>
  <h2>Values</h2>
  <div class="enum-grid">${rows}</div>
  <h2>Usage Example</h2>
  ${codeBlock('python', `from ftmgram import enums\n\n# Use as a value\nvalue = enums.${name}.${values[0].key}\nprint(value)  # Output: ${values[0].key.toLowerCase()}`)}`;
}

// ── All Pages ─────────────────────────────────────────────────
const PAGES = {

// ── HOME ─────────────────────────────────────────────────────
home: () => `
<div class="hero">
  <div class="hero-badge">✨ Bot API 10.1 — June 2026</div>
  <h1>FTMGram Documentation</h1>
  <p>Elegant, modern and asynchronous Telegram MTProto API framework in Python — for users and bots.</p>
  <div class="hero-actions">
    <button class="btn btn-primary" onclick="navigate('quickstart')">🚀 Quick Start</button>
    <button class="btn btn-secondary" onclick="navigate('install')">📦 Install</button>
    <a class="btn btn-secondary" href="https://github.com/ftmdevz/ftmgram" target="_blank">⭐ GitHub</a>
  </div>
</div>

${codeBlock('python', `from ftmgram import Client, filters

app = Client("my_account")

@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from FTMGram!")

app.run()`)}

<h2>Bot API 10.1 Coverage</h2>
<table class="badge-table">
  <thead><tr><th>Feature</th><th>Status</th></tr></thead>
  <tbody>
    <tr><td>Rich Messages — <code>send_rich_message</code>, <code>send_rich_message_draft</code></td><td class="check">✅</td></tr>
    <tr><td>RichText — 14 inline types (Bold, Italic, Url, Code, Marked…)</td><td class="check">✅</td></tr>
    <tr><td>RichBlock — 19 block types (Paragraph, Photo, Video, Table…)</td><td class="check">✅</td></tr>
    <tr><td>Checklist media — <code>MessageMediaType.CHECKLIST</code></td><td class="check">✅</td></tr>
    <tr><td>Link poll media — <code>MessageMediaType.LINK</code></td><td class="check">✅</td></tr>
    <tr><td>Chat join request queries — <code>answer_chat_join_request_query</code></td><td class="check">✅</td></tr>
    <tr><td><code>User.supports_join_request_queries</code>, <code>Chat.guard_bot</code></td><td class="check">✅</td></tr>
    <tr><td>Owned star balance — <code>get_owned_star_count</code></td><td class="check">✅</td></tr>
  </tbody>
</table>

<h2>Key Features</h2>
<div class="feature-grid">
  <div class="feature-card"><div class="icon">⚡</div><h3>Fast</h3><p>Powered by TgCrypto — a C-level cryptography library.</p></div>
  <div class="feature-card"><div class="icon">🎯</div><h3>Easy</h3><p>Clean Pythonic API that hides MTProto complexity.</p></div>
  <div class="feature-card"><div class="icon">🔷</div><h3>Type-hinted</h3><p>Full annotations for excellent IDE support.</p></div>
  <div class="feature-card"><div class="icon">🔄</div><h3>Async</h3><p>Fully asynchronous; synchronous usage also supported.</p></div>
  <div class="feature-card"><div class="icon">🤖</div><h3>Bot API 10.1</h3><p>Latest Telegram features covered on day one.</p></div>
  <div class="feature-card"><div class="icon">🔌</div><h3>Drop-in</h3><p>Zero-friction migration from Pyrogram or KuriGram.</p></div>
</div>`,

// ── INSTALL ──────────────────────────────────────────────────
install: () => `
${breadcrumb('Getting Started', 'Installation')}
<h1>Installation</h1>
<p>FTMGram requires Python 3.8 or higher. Install via pip from PyPI or directly from GitHub.</p>

<h2>Stable Release (PyPI)</h2>
${codeBlock('bash', 'pip install ftmgram')}

<h2>Latest from GitHub</h2>
${codeBlock('bash', 'pip install https://github.com/ftmdevz/ftmgram/archive/ftmdevz.zip --force-reinstall')}

<h2>With TgCrypto (Recommended)</h2>
<p>TgCrypto is a high-performance C library that speeds up encryption. Install it alongside FTMGram:</p>
${codeBlock('bash', 'pip install ftmgram tgcrypto')}

<h2>Dependencies</h2>
${paramsTable([
  { name: 'Python', type: '≥ 3.8', required: true, desc: 'Core runtime' },
  { name: 'tgcrypto', type: 'optional', required: false, desc: 'Fast crypto (strongly recommended)' },
  { name: 'aiohttp', type: 'installed automatically', required: false, desc: 'Async HTTP client' },
  { name: 'qrcode', type: 'optional', required: false, desc: 'QR code login support' },
])}

<div class="tip-box"><div><strong>Tip:</strong> Always use a virtual environment: <code>python -m venv venv && source venv/bin/activate</code></div></div>`,

// ── QUICKSTART ───────────────────────────────────────────────
quickstart: () => `
${breadcrumb('Getting Started', 'Quick Start')}
<h1>Quick Start</h1>
<p>Get a working Telegram bot or user client running in under 2 minutes.</p>

<h2>1. Get your API credentials</h2>
<p>Visit <a href="https://my.telegram.org" target="_blank">my.telegram.org</a> → API development tools → create an app. You will get <code>api_id</code> and <code>api_hash</code>.</p>

<h2>2. Your first bot</h2>
${codeBlock('python', `from ftmgram import Client, filters

# Replace with your own values from @BotFather
app = Client(
    "my_bot",
    api_id=12345,
    api_hash="your_api_hash",
    bot_token="123456:ABC-your-bot-token"
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("👋 Hello! I'm powered by FTMGram.")

@app.on_message(filters.command("ping"))
async def ping(client, message):
    await message.reply("🏓 Pong!")

app.run()`)}

<h2>3. User client (interactive login)</h2>
${codeBlock('python', `from ftmgram import Client

app = Client("my_account", api_id=12345, api_hash="your_api_hash")

async def main():
    async with app:
        me = await app.get_me()
        print(f"Logged in as {me.first_name}")

app.run(main())`)}

<h2>4. Using filters</h2>
${codeBlock('python', `from ftmgram import Client, filters
from ftmgram import types

app = Client("my_bot", api_id=12345, api_hash="hash", bot_token="token")

# Only respond to private messages
@app.on_message(filters.private & filters.text)
async def echo(client, message):
    await message.reply(message.text)

# Respond to photos in groups
@app.on_message(filters.group & filters.photo)
async def on_photo(client, message):
    await message.reply("Nice photo! 📸")

app.run()`)}

<h2>5. Inline keyboards</h2>
${codeBlock('python', `from ftmgram import Client, filters
from ftmgram.types import InlineKeyboardMarkup, InlineKeyboardButton

app = Client("my_bot", bot_token="token")

@app.on_message(filters.command("menu"))
async def menu(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📖 Docs", url="https://ftmdevz.github.io/ftmgram")],
        [InlineKeyboardButton("✅ Confirm", callback_data="confirm"),
         InlineKeyboardButton("❌ Cancel",  callback_data="cancel")]
    ])
    await message.reply("Choose an option:", reply_markup=keyboard)

@app.on_callback_query()
async def on_button(client, query):
    await query.answer(f"You clicked: {query.data}", show_alert=True)

app.run()`)}`,

// ── CLIENT ───────────────────────────────────────────────────
client: () => `
${breadcrumb('Getting Started', 'Client')}
<h1>Client</h1>
<p>The <code>Client</code> class is the main entry point for interacting with Telegram. It manages connection, authentication, and dispatches updates.</p>

<h2>Constructor</h2>
${codeBlock('python', `from ftmgram import Client

app = Client(
    name,               # Session name (str)
    api_id=None,        # From my.telegram.org (int)
    api_hash=None,      # From my.telegram.org (str)
    bot_token=None,     # From @BotFather — makes this a bot (str)
    session_string=None,# Restore existing session (str)
    in_memory=False,    # Keep session in memory only (bool)
    phone_number=None,  # Auto-login phone number (str)
    workdir=".",        # Directory to store session file (str)
    no_updates=False,   # Disable update handling (bool)
)`)}

${paramsTable([
  { name: 'name', type: 'str', required: true, desc: 'A name for the session file. E.g. "my_bot" creates my_bot.session.' },
  { name: 'api_id', type: 'int', required: true, desc: 'Your Telegram API ID from my.telegram.org.' },
  { name: 'api_hash', type: 'str', required: true, desc: 'Your Telegram API hash from my.telegram.org.' },
  { name: 'bot_token', type: 'str', required: false, desc: 'Bot token from @BotFather. Enables bot mode.' },
  { name: 'session_string', type: 'str', required: false, desc: 'Restore a session from a previously exported string.' },
  { name: 'in_memory', type: 'bool', required: false, desc: 'Store session in memory instead of disk.' },
  { name: 'no_updates', type: 'bool', required: false, desc: 'Disable update dispatching (useful for scripts).' },
  { name: 'workdir', type: 'str', required: false, desc: 'Directory where session files are saved.' },
])}

<h2>Usage as context manager</h2>
${codeBlock('python', `from ftmgram import Client

async def main():
    async with Client("my_account", api_id=12345, api_hash="hash") as app:
        me = await app.get_me()
        print(me.first_name)

import asyncio
asyncio.run(main())`)}

<h2>Multi-client</h2>
${codeBlock('python', `from ftmgram import Client, compose

app1 = Client("account1", api_id=1, api_hash="hash1")
app2 = Client("account2", api_id=2, api_hash="hash2")

compose([app1, app2])`)}`,

// ══════════════════════════════════════════════════════════════
// MESSAGES
// ══════════════════════════════════════════════════════════════

send_message: () => `
${breadcrumb('Messages', 'send_message')}
${methodHeader('send_message', 'Send a text message to a chat.', ['users','bots','async'])}

<h2>Signature</h2>
${codeBlock('python', `await app.send_message(
    chat_id,                          # int | str  — required
    text,                             # str        — required
    parse_mode=None,                  # enums.ParseMode
    entities=None,                    # List[MessageEntity]
    link_preview_options=None,        # LinkPreviewOptions
    disable_notification=None,        # bool
    message_thread_id=None,           # int  (forum topic)
    effect_id=None,                   # int  (private chats)
    reply_parameters=None,            # ReplyParameters
    schedule_date=None,               # datetime
    protect_content=None,             # bool
    business_connection_id=None,      # str
    reply_markup=None,                # InlineKeyboardMarkup | ReplyKeyboardMarkup | ...
)`)}

<h2>Parameters</h2>
${paramsTable([
  { name:'chat_id', type:'int | str', required:true, desc:'Target chat ID, username, "me" or phone number.' },
  { name:'text', type:'str', required:true, desc:'Text of the message to send. Up to 4096 characters.' },
  { name:'parse_mode', type:'enums.ParseMode', required:false, desc:'ParseMode.HTML, ParseMode.MARKDOWN, or ParseMode.DEFAULT.' },
  { name:'entities', type:'List[MessageEntity]', required:false, desc:'Special formatting entities instead of parse_mode.' },
  { name:'link_preview_options', type:'LinkPreviewOptions', required:false, desc:'Control link preview generation.' },
  { name:'disable_notification', type:'bool', required:false, desc:'Send silently — no sound notification.' },
  { name:'message_thread_id', type:'int', required:false, desc:'Forum topic ID. Forums only.' },
  { name:'reply_parameters', type:'ReplyParameters', required:false, desc:'Reply to a specific message.' },
  { name:'schedule_date', type:'datetime', required:false, desc:'Schedule the message for a future date.' },
  { name:'protect_content', type:'bool', required:false, desc:'Prevent forwarding and saving.' },
  { name:'reply_markup', type:'InlineKeyboardMarkup | ...', required:false, desc:'Inline or reply keyboard.' },
])}

${returns('types.Message', 'On success, the sent Message object is returned.')}

<h2>Examples</h2>

<h4>Basic message</h4>
${codeBlock('python', `await app.send_message("me", "Hello, World!")`)}

<h4>With Markdown formatting</h4>
${codeBlock('python', `from ftmgram import enums

await app.send_message(
    "username",
    "**Bold**, __italic__, \`code\`",
    parse_mode=enums.ParseMode.MARKDOWN
)`)}

<h4>Reply to a message</h4>
${codeBlock('python', `from ftmgram.types import ReplyParameters

await app.send_message(
    chat_id,
    "This is a reply!",
    reply_parameters=ReplyParameters(message_id=123)
)`)}

<h4>With inline keyboard</h4>
${codeBlock('python', `from ftmgram.types import InlineKeyboardMarkup, InlineKeyboardButton

await app.send_message(
    chat_id,
    "Click a button:",
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Docs", url="https://ftmdevz.github.io/ftmgram")],
        [InlineKeyboardButton("Callback", callback_data="hello")]
    ])
)`)}

<h4>Scheduled message</h4>
${codeBlock('python', `from datetime import datetime, timedelta

await app.send_message(
    chat_id,
    "This message was scheduled!",
    schedule_date=datetime.now() + timedelta(hours=1)
)`)}`,

// ─────────────────────────────────────────────────────────────
send_photo: () => `
${breadcrumb('Messages', 'send_photo')}
${methodHeader('send_photo', 'Send photos to a chat. Supports file path, URL, file-like object, or file_id.', ['users','bots','async'])}

<h2>Signature</h2>
${codeBlock('python', `await app.send_photo(
    chat_id,
    photo,                   # str | BinaryIO — file path, URL, file_id or BinaryIO
    caption="",              # str
    parse_mode=None,         # enums.ParseMode
    has_spoiler=None,        # bool
    ttl_seconds=None,        # int — self-destruct timer
    disable_notification=None,
    reply_parameters=None,
    protect_content=None,
    reply_markup=None,
    progress=None,           # Callable — upload progress callback
)`)}

<h2>Parameters</h2>
${paramsTable([
  { name:'chat_id', type:'int | str', required:true, desc:'Target chat.' },
  { name:'photo', type:'str | BinaryIO', required:true, desc:'File path, Telegram file_id, HTTP URL, or file-like object.' },
  { name:'caption', type:'str', required:false, desc:'Caption text, up to 1024 characters.' },
  { name:'parse_mode', type:'enums.ParseMode', required:false, desc:'Caption parse mode.' },
  { name:'has_spoiler', type:'bool', required:false, desc:'Blurs the photo as a spoiler.' },
  { name:'ttl_seconds', type:'int', required:false, desc:'Self-destruct timer (users only).' },
  { name:'progress', type:'Callable', required:false, desc:'Callback for upload progress.' },
])}
${returns('types.Message', 'The sent message with the photo.')}

<h2>Examples</h2>
<h4>From local file</h4>
${codeBlock('python', `await app.send_photo("me", "photo.jpg", caption="My photo!")`)}

<h4>From URL</h4>
${codeBlock('python', `await app.send_photo(chat_id, "https://example.com/image.png", caption="From URL")`)}

<h4>With spoiler</h4>
${codeBlock('python', `await app.send_photo(chat_id, "photo.jpg", has_spoiler=True)`)}

<h4>With progress tracking</h4>
${codeBlock('python', `async def progress(current, total):
    print(f"Uploaded {current * 100 / total:.1f}%")

await app.send_photo(chat_id, "big_photo.jpg", progress=progress)`)}`,

// ─────────────────────────────────────────────────────────────
send_audio: () => `
${breadcrumb('Messages', 'send_audio')}
${methodHeader('send_audio', 'Send audio files. Telegram treats these as music in the music player.', ['users','bots','async'])}
<h2>Signature</h2>
${codeBlock('python', `await app.send_audio(
    chat_id,
    audio,               # str | BinaryIO
    caption="",
    parse_mode=None,
    duration=0,          # int — seconds
    performer=None,      # str
    title=None,          # str
    thumb=None,          # str | BinaryIO — thumbnail
    file_name=None,      # str
    disable_notification=None,
    reply_parameters=None,
    protect_content=None,
    reply_markup=None,
    progress=None,
)`)}
${paramsTable([
  { name:'chat_id', type:'int | str', required:true, desc:'Target chat.' },
  { name:'audio', type:'str | BinaryIO', required:true, desc:'Audio file path, file_id, URL or BinaryIO.' },
  { name:'duration', type:'int', required:false, desc:'Duration of the audio in seconds.' },
  { name:'performer', type:'str', required:false, desc:'Performer name shown in the music player.' },
  { name:'title', type:'str', required:false, desc:'Track title shown in the music player.' },
  { name:'thumb', type:'str | BinaryIO', required:false, desc:'Thumbnail image.' },
])}
${returns('types.Message','The sent message with audio.')}
<h2>Example</h2>
${codeBlock('python', `await app.send_audio(
    chat_id,
    "song.mp3",
    caption="🎵 My favourite song",
    performer="Artist Name",
    title="Song Title",
    duration=210
)`)}`,

// ─────────────────────────────────────────────────────────────
send_video: () => `
${breadcrumb('Messages', 'send_video')}
${methodHeader('send_video', 'Send video files.', ['users','bots','async'])}
<h2>Signature</h2>
${codeBlock('python', `await app.send_video(
    chat_id,
    video,              # str | BinaryIO
    caption="",
    parse_mode=None,
    duration=0,
    width=0,
    height=0,
    thumb=None,
    file_name=None,
    supports_streaming=True,
    has_spoiler=None,
    ttl_seconds=None,
    disable_notification=None,
    reply_parameters=None,
    protect_content=None,
    reply_markup=None,
    progress=None,
)`)}
${paramsTable([
  { name:'video', type:'str | BinaryIO', required:true, desc:'Video file path, file_id, URL or BinaryIO.' },
  { name:'duration', type:'int', required:false, desc:'Duration in seconds.' },
  { name:'width', type:'int', required:false, desc:'Video width.' },
  { name:'height', type:'int', required:false, desc:'Video height.' },
  { name:'supports_streaming', type:'bool', required:false, desc:'Enable streaming. Default True.' },
  { name:'has_spoiler', type:'bool', required:false, desc:'Blurs as spoiler.' },
])}
${returns('types.Message','The sent message with video.')}
<h2>Example</h2>
${codeBlock('python', `await app.send_video(
    chat_id,
    "clip.mp4",
    caption="Watch this! 🎬",
    supports_streaming=True
)`)}`,

// ─────────────────────────────────────────────────────────────
send_document: () => `
${breadcrumb('Messages', 'send_document')}
${methodHeader('send_document', 'Send any file as a document.', ['users','bots','async'])}
<h2>Signature</h2>
${codeBlock('python', `await app.send_document(
    chat_id,
    document,           # str | BinaryIO
    thumb=None,
    caption="",
    parse_mode=None,
    file_name=None,
    force_document=None,
    disable_notification=None,
    reply_parameters=None,
    protect_content=None,
    reply_markup=None,
    progress=None,
)`)}
${returns('types.Message','The sent document message.')}
<h2>Example</h2>
${codeBlock('python', `await app.send_document(
    chat_id,
    "report.pdf",
    caption="Monthly report 📎",
    file_name="report_june_2026.pdf"
)`)}`,

// ─────────────────────────────────────────────────────────────
send_animation: () => `
${breadcrumb('Messages', 'send_animation')}
${methodHeader('send_animation', 'Send animation files (GIF or H.264/MPEG-4 AVC video without sound).', ['users','bots','async'])}
${codeBlock('python', `await app.send_animation(
    chat_id,
    animation,          # str | BinaryIO
    caption="",
    parse_mode=None,
    duration=0,
    width=0,
    height=0,
    thumb=None,
    has_spoiler=None,
    reply_parameters=None,
    protect_content=None,
    reply_markup=None,
    progress=None,
)`)}
<h2>Example</h2>
${codeBlock('python', `await app.send_animation(chat_id, "funny.gif", caption="LOL 😂")`)}`,

// ─────────────────────────────────────────────────────────────
send_sticker: () => `
${breadcrumb('Messages', 'send_sticker')}
${methodHeader('send_sticker', 'Send a sticker.', ['users','bots','async'])}
${codeBlock('python', `await app.send_sticker(
    chat_id,
    sticker,        # str | BinaryIO — file_id or file
    emoji=None,     # str
    reply_parameters=None,
    reply_markup=None,
)`)}
<h2>Example</h2>
${codeBlock('python', `# Send by file_id
await app.send_sticker(chat_id, "CAACAgIAAxkBAAIBcmJ...")

# Send from file
await app.send_sticker(chat_id, "sticker.webp")`)}`,

// ─────────────────────────────────────────────────────────────
send_voice: () => `
${breadcrumb('Messages', 'send_voice')}
${methodHeader('send_voice', 'Send an audio file as a voice message. File must be in OGG format encoded with OPUS.', ['users','bots','async'])}
${codeBlock('python', `await app.send_voice(
    chat_id,
    voice,          # str | BinaryIO
    caption="",
    parse_mode=None,
    duration=0,
    reply_parameters=None,
    protect_content=None,
    reply_markup=None,
    progress=None,
)`)}
<h2>Example</h2>
${codeBlock('python', `await app.send_voice(chat_id, "voice_note.ogg", duration=5)`)}`,

// ─────────────────────────────────────────────────────────────
send_video_note: () => `
${breadcrumb('Messages', 'send_video_note')}
${methodHeader('send_video_note', 'Send a rounded video note (telegram video circles).', ['users','bots','async'])}
${codeBlock('python', `await app.send_video_note(
    chat_id,
    video_note,     # str | BinaryIO
    duration=0,
    length=1,       # int — video width & height
    thumb=None,
    reply_parameters=None,
    protect_content=None,
    progress=None,
)`)}
<h2>Example</h2>
${codeBlock('python', `await app.send_video_note(chat_id, "circle.mp4", duration=15, length=240)`)}`,

// ─────────────────────────────────────────────────────────────
send_location: () => `
${breadcrumb('Messages', 'send_location')}
${methodHeader('send_location', 'Send a point on the map.', ['users','bots','async'])}
${codeBlock('python', `await app.send_location(
    chat_id,
    latitude,           # float
    longitude,          # float
    horizontal_accuracy=None,  # float (0-1500 meters)
    live_period=None,   # int — seconds for live location
    heading=None,       # int — 1-360 degrees
    proximity_alert_radius=None,
    reply_parameters=None,
    reply_markup=None,
)`)}
<h2>Example</h2>
${codeBlock('python', `# Static location
await app.send_location(chat_id, 28.6139, 77.2090)  # New Delhi

# Live location (60 seconds)
await app.send_location(chat_id, 28.6139, 77.2090, live_period=60)`)}`,

// ─────────────────────────────────────────────────────────────
send_contact: () => `
${breadcrumb('Messages', 'send_contact')}
${methodHeader('send_contact', 'Send a phone contact.', ['users','bots','async'])}
${codeBlock('python', `await app.send_contact(
    chat_id,
    phone_number,       # str
    first_name,         # str
    last_name=None,     # str
    vcard=None,         # str — vCard 3.0 data
    reply_parameters=None,
    reply_markup=None,
)`)}
<h2>Example</h2>
${codeBlock('python', `await app.send_contact(chat_id, "+91987654321", "Rahul", "Sharma")`)}`,

// ─────────────────────────────────────────────────────────────
send_poll: () => `
${breadcrumb('Messages', 'send_poll')}
${methodHeader('send_poll', 'Send a native poll.', ['users','bots','async'])}
${codeBlock('python', `await app.send_poll(
    chat_id,
    question,               # str
    options,                # List[str] — 2-10 options
    is_anonymous=True,      # bool
    type=PollType.REGULAR,  # enums.PollType
    allows_multiple_answers=False,
    correct_option_id=None, # int — for quiz polls
    explanation=None,       # str
    open_period=None,       # int — seconds
    reply_parameters=None,
    protect_content=None,
)`)}
<h2>Example</h2>
${codeBlock('python', `from ftmgram import enums

# Regular poll
await app.send_poll(
    chat_id,
    "What's your favourite language?",
    ["Python 🐍", "JavaScript", "Rust", "Go"]
)

# Quiz
await app.send_poll(
    chat_id,
    "Capital of India?",
    ["Mumbai", "New Delhi", "Chennai"],
    type=enums.PollType.QUIZ,
    correct_option_id=1,
    explanation="New Delhi is the capital."
)`)}`,

// ─────────────────────────────────────────────────────────────
send_dice: () => `
${breadcrumb('Messages', 'send_dice')}
${methodHeader('send_dice', 'Send an animated emoji that displays a random value.', ['users','bots','async'])}
${codeBlock('python', `await app.send_dice(
    chat_id,
    emoji="🎲",     # str — 🎲 🎯 🏀 ⚽ 🎳 🎰
    reply_parameters=None,
    protect_content=None,
)`)}
<h2>Example</h2>
${codeBlock('python', `# Roll a dice
msg = await app.send_dice(chat_id, emoji="🎲")
print(f"Rolled: {msg.dice.value}")

# Spin a slot machine
await app.send_dice(chat_id, emoji="🎰")`)}`,

// ─────────────────────────────────────────────────────────────
send_media_group: () => `
${breadcrumb('Messages', 'send_media_group')}
${methodHeader('send_media_group', 'Send a group of photos, videos, or documents as an album.', ['users','bots','async'])}
${codeBlock('python', `await app.send_media_group(
    chat_id,
    media,              # List[InputMediaPhoto | InputMediaVideo | InputMediaDocument | InputMediaAudio]
    disable_notification=None,
    message_thread_id=None,
    reply_parameters=None,
    protect_content=None,
)`)}
<h2>Example</h2>
${codeBlock('python', `from ftmgram.types import InputMediaPhoto, InputMediaVideo

await app.send_media_group(
    chat_id,
    [
        InputMediaPhoto("photo1.jpg", caption="First photo"),
        InputMediaPhoto("photo2.jpg"),
        InputMediaVideo("clip.mp4", caption="And a video!"),
    ]
)`)}`,

// ─────────────────────────────────────────────────────────────
send_rich_message: () => `
${breadcrumb('Messages', 'send_rich_message')}
${methodHeader('send_rich_message', 'Send a rich structured message with blocks (Bot API 10.1). Bots only.', ['bots','async','new'])}

<div class="note-box"><strong>Bot API 10.1:</strong> This method is exclusive to FTMGram v3+ and uses Telegram\'s new rich content system.</div>

<h2>Signature</h2>
${codeBlock('python', `await app.send_rich_message(
    chat_id,
    rich_message,                   # types.InputRichMessage — required
    disable_notification=None,
    message_thread_id=None,
    reply_parameters=None,
    protect_content=None,
    business_connection_id=None,
    allow_paid_broadcast=None,
    suggested_post_parameters=None,
    reply_markup=None,
)`)}

<h2>Parameters</h2>
${paramsTable([
  { name:'chat_id', type:'int | str', required:true, desc:'Target chat.' },
  { name:'rich_message', type:'types.InputRichMessage', required:true, desc:'The rich message content containing title, blocks and optional buttons.' },
])}
${returns('types.Message','The sent rich message.')}

<h2>Example</h2>
${codeBlock('python', `from ftmgram import Client
from ftmgram.types import (
    InputRichMessage, RichText, RichBlock,
    RichTextPlain, RichTextBold, RichBlockParagraph, RichBlockPhoto
)

app = Client("my_bot", bot_token="TOKEN")

async def main():
    async with app:
        await app.send_rich_message(
            chat_id=123456,
            rich_message=InputRichMessage(
                title=RichText([RichTextBold("FTMGram Guide")]),
                blocks=[
                    RichBlockParagraph(
                        text=RichText([
                            RichTextPlain("Welcome to "),
                            RichTextBold("FTMGram"),
                            RichTextPlain(" — the most powerful Telegram library!"),
                        ])
                    ),
                ]
            )
        )

app.run(main())`)}`,

// ─────────────────────────────────────────────────────────────
send_checklist: () => `
${breadcrumb('Messages', 'send_checklist')}
${methodHeader('send_checklist', 'Send an interactive checklist message (Bot API 10.1). Bots only.', ['bots','async','new'])}

<div class="note-box"><strong>Bot API 10.1:</strong> Checklists are a new Telegram media type exclusive to FTMGram v3+.</div>

<h2>Signature</h2>
${codeBlock('python', `await app.send_checklist(
    chat_id,
    title,              # str — checklist title
    tasks,              # List[InputChecklistTask]
    others_can_add=None,    # bool — allow others to add tasks
    others_can_complete=None, # bool — allow others to complete tasks
    disable_notification=None,
    reply_parameters=None,
    protect_content=None,
    reply_markup=None,
)`)}

${paramsTable([
  { name:'title', type:'str', required:true, desc:'Title of the checklist.' },
  { name:'tasks', type:'List[InputChecklistTask]', required:true, desc:'List of tasks in the checklist.' },
  { name:'others_can_add', type:'bool', required:false, desc:'Allow other users to add new tasks.' },
  { name:'others_can_complete', type:'bool', required:false, desc:'Allow other users to mark tasks as done.' },
])}
${returns('types.Message','The sent checklist message.')}

<h2>Example</h2>
${codeBlock('python', `from ftmgram.types import InputChecklistTask

await app.send_checklist(
    chat_id,
    title="Shopping List 🛒",
    tasks=[
        InputChecklistTask("Buy milk"),
        InputChecklistTask("Buy bread"),
        InputChecklistTask("Buy eggs"),
    ],
    others_can_complete=True
)`)}`,

// ─────────────────────────────────────────────────────────────
forward_message: () => `
${breadcrumb('Messages', 'forward_message')}
${methodHeader('forward_message', 'Forward a message from one chat to another.', ['users','bots','async'])}
${codeBlock('python', `await app.forward_message(
    chat_id,
    from_chat_id,
    message_id,
    message_thread_id=None,
    disable_notification=None,
    protect_content=None,
    reply_parameters=None,
)`)}
${paramsTable([
  { name:'chat_id', type:'int | str', required:true, desc:'Destination chat.' },
  { name:'from_chat_id', type:'int | str', required:true, desc:'Source chat where the original message exists.' },
  { name:'message_id', type:'int', required:true, desc:'ID of the message to forward.' },
])}
${returns('types.Message','The forwarded message.')}
<h2>Example</h2>
${codeBlock('python', `# Forward message 42 from @channelname to me
await app.forward_message("me", "@channelname", 42)`)}`,

// ─────────────────────────────────────────────────────────────
copy_message: () => `
${breadcrumb('Messages', 'copy_message')}
${methodHeader('copy_message', 'Copy a message — like forward but without "Forwarded from" attribution.', ['users','bots','async'])}
${codeBlock('python', `await app.copy_message(
    chat_id,
    from_chat_id,
    message_id,
    caption=None,
    parse_mode=None,
    caption_entities=None,
    disable_notification=None,
    reply_parameters=None,
    reply_markup=None,
)`)}
${returns('types.Message','The copied message.')}
<h2>Example</h2>
${codeBlock('python', `await app.copy_message(destination_chat, source_chat, message_id=42)`)}`,

// ─────────────────────────────────────────────────────────────
edit_message_text: () => `
${breadcrumb('Messages', 'edit_message_text')}
${methodHeader('edit_message_text', 'Edit the text of a message.', ['users','bots','async'])}
${codeBlock('python', `await app.edit_message_text(
    chat_id,
    message_id,
    text,
    parse_mode=None,
    entities=None,
    link_preview_options=None,
    reply_markup=None,
)`)}
${paramsTable([
  { name:'chat_id', type:'int | str', required:true, desc:'Chat where the message exists.' },
  { name:'message_id', type:'int', required:true, desc:'ID of the message to edit.' },
  { name:'text', type:'str', required:true, desc:'New text content.' },
])}
${returns('types.Message','The edited message.')}
<h2>Example</h2>
${codeBlock('python', `# Send then edit
msg = await app.send_message(chat_id, "Original text")
await app.edit_message_text(chat_id, msg.id, "Edited text ✏️")`)}`,

// ─────────────────────────────────────────────────────────────
delete_message: () => `
${breadcrumb('Messages', 'delete_message')}
${methodHeader('delete_message', 'Delete one message.', ['users','bots','async'])}
${codeBlock('python', `await app.delete_message(
    chat_id,
    message_id,
    revoke=True,    # bool — delete for everyone
)`)}
${returns('bool','True on success.')}
<h2>Example</h2>
${codeBlock('python', `await app.delete_message(chat_id, message_id)

# Delete only for yourself (users only)
await app.delete_message(chat_id, message_id, revoke=False)`)}`,

// ─────────────────────────────────────────────────────────────
get_messages: () => `
${breadcrumb('Messages', 'get_messages')}
${methodHeader('get_messages', 'Fetch messages by ID from a chat.', ['users','bots','async'])}
${codeBlock('python', `await app.get_messages(
    chat_id,
    message_ids,        # int | List[int]
    reply_to_message_ids=None,
)`)}
${returns('types.Message | List[types.Message]','One or more message objects.')}
<h2>Example</h2>
${codeBlock('python', `# Single message
msg = await app.get_messages(chat_id, 42)

# Multiple messages
msgs = await app.get_messages(chat_id, [10, 11, 12])`)}`,

// ─────────────────────────────────────────────────────────────
get_chat_history: () => `
${breadcrumb('Messages', 'get_chat_history')}
${methodHeader('get_chat_history', 'Iterate over all messages in a chat, newest first.', ['users','async'])}
${codeBlock('python', `async for message in app.get_chat_history(
    chat_id,
    limit=0,            # int — 0 = all messages
    offset=0,           # int
    offset_id=0,        # int — start from this message ID
    offset_date=None,   # datetime
):
    print(message.text)`)}
<h2>Example</h2>
${codeBlock('python', `# Print last 100 messages
async for msg in app.get_chat_history(chat_id, limit=100):
    if msg.text:
        print(msg.text)

# Collect into list
history = [m async for m in app.get_chat_history(chat_id, limit=50)]`)}`,

// ─────────────────────────────────────────────────────────────
search_messages: () => `
${breadcrumb('Messages', 'search_messages')}
${methodHeader('search_messages', 'Search for messages in a chat matching a query string.', ['users','async'])}
${codeBlock('python', `async for message in app.search_messages(
    chat_id,
    query="",           # str — search query
    offset=0,
    filter=None,        # enums.MessagesFilter
    limit=0,
):
    print(message.text)`)}
<h2>Example</h2>
${codeBlock('python', `# Search text messages
async for msg in app.search_messages(chat_id, "hello", limit=20):
    print(msg.text)

# Search only photos
from ftmgram import enums
async for msg in app.search_messages(chat_id, filter=enums.MessagesFilter.PHOTO):
    print(msg.photo.file_id)`)}`,

// ─────────────────────────────────────────────────────────────
download_media: () => `
${breadcrumb('Messages', 'download_media')}
${methodHeader('download_media', 'Download the media in a message to your local disk.', ['users','bots','async'])}
${codeBlock('python', `path = await app.download_media(
    message,            # types.Message | str — message or file_id
    file_name=None,     # str — custom save path
    in_memory=False,    # bool — return BytesIO instead of saving
    block=True,
    progress=None,
    progress_args=(),
)`)}
${returns('str | BytesIO','File path on disk, or BytesIO if in_memory=True.')}
<h2>Example</h2>
${codeBlock('python', `@app.on_message(filters.photo)
async def save_photo(client, message):
    path = await message.download()
    print(f"Saved to {path}")

# Download to specific location
path = await app.download_media(message, file_name="downloads/photo.jpg")

# Download into memory
from io import BytesIO
buf = await app.download_media(message, in_memory=True)`)}`,

// ─────────────────────────────────────────────────────────────
send_chat_action: () => `
${breadcrumb('Messages', 'send_chat_action')}
${methodHeader('send_chat_action', 'Send a chat action (typing, uploading, etc.) to show user activity.', ['users','bots','async'])}
${codeBlock('python', `await app.send_chat_action(
    chat_id,
    action,             # enums.ChatAction
    message_thread_id=None,
)`)}
<h2>Example</h2>
${codeBlock('python', `from ftmgram import enums

await app.send_chat_action(chat_id, enums.ChatAction.TYPING)
# ... do something ...
await app.send_message(chat_id, "Done thinking!")

# Cancel action
await app.send_chat_action(chat_id, enums.ChatAction.CANCEL)`)}`,

// ─────────────────────────────────────────────────────────────
translate_message_text: () => `
${breadcrumb('Messages', 'translate_message_text')}
${methodHeader('translate_message_text', 'Translate a message text using Telegram\'s built-in translation API.', ['users','async'])}
${codeBlock('python', `result = await app.translate_message_text(
    chat_id,
    message_id,
    to_lang,        # str — language code e.g. "en", "hi", "de"
)`)}
<h2>Example</h2>
${codeBlock('python', `# Translate message 42 to Hindi
result = await app.translate_message_text(chat_id, 42, "hi")
print(result.text)`)}`,

// ══════════════════════════════════════════════════════════════
// CHATS
// ══════════════════════════════════════════════════════════════

get_chat: () => `
${breadcrumb('Chats', 'get_chat')}
${methodHeader('get_chat', 'Get up-to-date information about a chat — name, username, member count, etc.', ['users','bots','async'])}
${codeBlock('python', `chat = await app.get_chat(
    chat_id,            # int | str
    force_full=True,    # bool — fetch full info
)`)}
${paramsTable([
  { name:'chat_id', type:'int | str', required:true, desc:'Unique chat ID, username, invite link, or phone.' },
  { name:'force_full', type:'bool', required:false, desc:'Fetch complete chat info. Default True.' },
])}
${returns('types.Chat','Chat object with all available info.')}
<h2>Example</h2>
${codeBlock('python', `chat = await app.get_chat("telegram")
print(chat.title, chat.members_count)

# Get from message
chat = await app.get_chat(message.chat.id)`)}`,

// ─────────────────────────────────────────────────────────────
get_dialogs: () => `
${breadcrumb('Chats', 'get_dialogs')}
${methodHeader('get_dialogs', 'Iterate over all open dialogs (chats, groups, channels) of the current user.', ['users','async'])}
${codeBlock('python', `async for dialog in app.get_dialogs(limit=0):
    print(dialog.chat.title or dialog.chat.first_name)`)}
<h2>Example</h2>
${codeBlock('python', `# Print all dialog titles
async for d in app.get_dialogs():
    name = d.chat.title or d.chat.first_name or "Unknown"
    print(name)

# Collect first 20 dialogs
dialogs = [d async for d in app.get_dialogs(limit=20)]`)}`,

// ─────────────────────────────────────────────────────────────
join_chat: () => `
${breadcrumb('Chats', 'join_chat')}
${methodHeader('join_chat', 'Join a group or channel by username or invite link.', ['users','async'])}
${codeBlock('python', `chat = await app.join_chat(
    chat_id,        # int | str — username or invite link
)`)}
${returns('types.Chat','The joined chat.')}
<h2>Example</h2>
${codeBlock('python', `await app.join_chat("telegram")
await app.join_chat("https://t.me/joinchat/XXXXXX")`)}`,

// ─────────────────────────────────────────────────────────────
leave_chat: () => `
${breadcrumb('Chats', 'leave_chat')}
${methodHeader('leave_chat', 'Leave a group, supergroup or channel.', ['users','async'])}
${codeBlock('python', `await app.leave_chat(
    chat_id,
    delete=False,   # bool — also delete the dialog
)`)}
<h2>Example</h2>
${codeBlock('python', `await app.leave_chat(chat_id)
await app.leave_chat(chat_id, delete=True)  # also remove from list`)}`,

// ─────────────────────────────────────────────────────────────
create_group: () => `
${breadcrumb('Chats', 'create_group')}
${methodHeader('create_group', 'Create a new basic group.', ['users','async'])}
${codeBlock('python', `chat = await app.create_group(
    title,          # str — group name
    users,          # int | str | List[int|str] — initial members
)`)}
${returns('types.Chat','The created group.')}
<h2>Example</h2>
${codeBlock('python', `chat = await app.create_group("My Group", ["user1", "user2"])
print(chat.id)`)}`,

// ─────────────────────────────────────────────────────────────
create_channel: () => `
${breadcrumb('Chats', 'create_channel')}
${methodHeader('create_channel', 'Create a new channel.', ['users','async'])}
${codeBlock('python', `channel = await app.create_channel(
    title,          # str
    description="", # str
)`)}
<h2>Example</h2>
${codeBlock('python', `ch = await app.create_channel("My Channel", "A cool channel")
print(ch.id)`)}`,

// ─────────────────────────────────────────────────────────────
get_chat_members: () => `
${breadcrumb('Chats', 'get_chat_members')}
${methodHeader('get_chat_members', 'Iterate over the members of a group or channel.', ['users','bots','async'])}
${codeBlock('python', `async for member in app.get_chat_members(
    chat_id,
    query="",           # str — search query
    limit=0,
    filter=ChatMembersFilter.SEARCH,
):
    print(member.user.first_name)`)}
<h2>Example</h2>
${codeBlock('python', `from ftmgram import enums

# All admins
async for admin in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
    print(admin.user.first_name, admin.status)

# Search by name
async for m in app.get_chat_members(chat_id, query="John"):
    print(m.user.id)`)}`,

// ─────────────────────────────────────────────────────────────
ban_chat_member: () => `
${breadcrumb('Chats', 'ban_chat_member')}
${methodHeader('ban_chat_member', 'Ban a user from a group or channel.', ['users','bots','async'])}
${codeBlock('python', `await app.ban_chat_member(
    chat_id,
    user_id,            # int | str
    until_date=None,    # datetime — unban date
)`)}
<h2>Example</h2>
${codeBlock('python', `from datetime import datetime, timedelta

# Permanent ban
await app.ban_chat_member(chat_id, user_id)

# Temporary ban (1 day)
await app.ban_chat_member(
    chat_id, user_id,
    until_date=datetime.now() + timedelta(days=1)
)`)}`,

// ─────────────────────────────────────────────────────────────
promote_chat_member: () => `
${breadcrumb('Chats', 'promote_chat_member')}
${methodHeader('promote_chat_member', 'Promote or demote a user in a supergroup or channel.', ['users','bots','async'])}
${codeBlock('python', `await app.promote_chat_member(
    chat_id,
    user_id,
    privileges=None,    # ChatPrivileges
)`)}
<h2>Example</h2>
${codeBlock('python', `from ftmgram.types import ChatPrivileges

await app.promote_chat_member(
    chat_id, user_id,
    privileges=ChatPrivileges(
        can_manage_chat=True,
        can_delete_messages=True,
        can_restrict_members=True,
    )
)

# Demote (remove all privileges)
await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges())`)}`,

// ─────────────────────────────────────────────────────────────
set_chat_title: () => `
${breadcrumb('Chats', 'set_chat_title')}
${methodHeader('set_chat_title', 'Set the title of a group, supergroup or channel.', ['users','bots','async'])}
${codeBlock('python', `await app.set_chat_title(chat_id, title)`)}
<h2>Example</h2>
${codeBlock('python', `await app.set_chat_title(chat_id, "New Group Name 🎉")`)}`,

// ─────────────────────────────────────────────────────────────
pin_chat_message: () => `
${breadcrumb('Chats', 'pin_chat_message')}
${methodHeader('pin_chat_message', 'Pin a message in a chat.', ['users','bots','async'])}
${codeBlock('python', `await app.pin_chat_message(
    chat_id,
    message_id,
    disable_notification=False,
    both_sides=False,   # bool — pin for both sides in PM
)`)}
<h2>Example</h2>
${codeBlock('python', `await app.pin_chat_message(chat_id, message_id, disable_notification=True)`)}`,

// ─────────────────────────────────────────────────────────────
get_chat_event_log: () => `
${breadcrumb('Chats', 'get_chat_event_log')}
${methodHeader('get_chat_event_log', 'Iterate over the administrator event log of a supergroup or channel.', ['users','async'])}
${codeBlock('python', `async for event in app.get_chat_event_log(
    chat_id,
    query="",
    offset_id=0,
    limit=0,
    filters=None,       # ChatEventFilter
    user_ids=None,      # List[int|str]
):
    print(event.action)`)}
<h2>Example</h2>
${codeBlock('python', `async for event in app.get_chat_event_log(chat_id, limit=50):
    print(event.date, event.action)`)}`,

// ══════════════════════════════════════════════════════════════
// USERS
// ══════════════════════════════════════════════════════════════

get_me: () => `
${breadcrumb('Users', 'get_me')}
${methodHeader('get_me', 'Get your own user identity. Returns info about the logged-in account.', ['users','bots','async'])}
${codeBlock('python', `me = await app.get_me()`)}
${returns('types.User','The User object for the logged-in account.')}
<h2>Example</h2>
${codeBlock('python', `me = await app.get_me()
print(f"ID: {me.id}")
print(f"Name: {me.first_name} {me.last_name or ''}")
print(f"Username: @{me.username}")
print(f"Is bot: {me.is_bot}")`)}`,

// ─────────────────────────────────────────────────────────────
get_users: () => `
${breadcrumb('Users', 'get_users')}
${methodHeader('get_users', 'Get the User object(s) for one or more user IDs or usernames.', ['users','bots','async'])}
${codeBlock('python', `users = await app.get_users(
    user_ids,       # int | str | List[int|str]
)`)}
${returns('types.User | List[types.User]','One or a list of User objects.')}
<h2>Example</h2>
${codeBlock('python', `# Single user
user = await app.get_users("telegram")
print(user.first_name)

# Multiple users
users = await app.get_users([123, 456, "@username"])
for u in users:
    print(u.id, u.first_name)`)}`,

// ─────────────────────────────────────────────────────────────
get_user_profile_photos: () => `
${breadcrumb('Users', 'get_user_profile_photos')}
${methodHeader('get_user_profile_photos', 'Iterate over the profile photos of a user.', ['users','bots','async'])}
${codeBlock('python', `async for photo in app.get_user_profile_photos(
    user_id,
    offset=0,
    limit=0,
):
    print(photo.file_id)`)}
<h2>Example</h2>
${codeBlock('python', `async for photo in app.get_user_profile_photos("me", limit=5):
    await app.download_media(photo)`)}`,

// ─────────────────────────────────────────────────────────────
block_user: () => `
${breadcrumb('Users', 'block_user')}
${methodHeader('block_user', 'Block a user.', ['users','async'])}
${codeBlock('python', `await app.block_user(user_id)`)}
<h2>Example</h2>
${codeBlock('python', `await app.block_user(user_id)
print("User blocked")`)}`,

// ─────────────────────────────────────────────────────────────
unblock_user: () => `
${breadcrumb('Users', 'unblock_user')}
${methodHeader('unblock_user', 'Unblock a previously blocked user.', ['users','async'])}
${codeBlock('python', `await app.unblock_user(user_id)`)}
<h2>Example</h2>
${codeBlock('python', `await app.unblock_user(user_id)
print("User unblocked")`)}`,

// ─────────────────────────────────────────────────────────────
update_profile: () => `
${breadcrumb('Users', 'update_profile')}
${methodHeader('update_profile', 'Update your account profile (name, bio).', ['users','async'])}
${codeBlock('python', `await app.update_profile(
    first_name=None,
    last_name=None,
    bio=None,
)`)}
<h2>Example</h2>
${codeBlock('python', `await app.update_profile(
    first_name="Rahul",
    last_name="Dev",
    bio="Building cool bots with FTMGram 🚀"
)`)}`,

// ─────────────────────────────────────────────────────────────
set_profile_photo: () => `
${breadcrumb('Users', 'set_profile_photo')}
${methodHeader('set_profile_photo', 'Set a new profile photo.', ['users','async'])}
${codeBlock('python', `await app.set_profile_photo(
    photo=None,     # str | BinaryIO — photo file
    video=None,     # str | BinaryIO — animated profile video
)`)}
<h2>Example</h2>
${codeBlock('python', `await app.set_profile_photo(photo="avatar.jpg")`)}`,

// ══════════════════════════════════════════════════════════════
// BOTS
// ══════════════════════════════════════════════════════════════

answer_callback_query: () => `
${breadcrumb('Bots', 'answer_callback_query')}
${methodHeader('answer_callback_query', 'Answer an incoming callback query from an inline keyboard button.', ['bots','async'])}
${codeBlock('python', `await app.answer_callback_query(
    callback_query_id,  # str
    text=None,          # str — notification text
    show_alert=False,   # bool — show as alert popup
    url=None,           # str — open URL
    cache_time=0,       # int — cache duration
)`)}
<h2>Example</h2>
${codeBlock('python', `@app.on_callback_query()
async def handle(client, query):
    if query.data == "confirm":
        await query.answer("✅ Confirmed!", show_alert=True)
    elif query.data == "cancel":
        await query.answer("❌ Cancelled")`)}`,

// ─────────────────────────────────────────────────────────────
answer_inline_query: () => `
${breadcrumb('Bots', 'answer_inline_query')}
${methodHeader('answer_inline_query', 'Answer an inline query with a list of results.', ['bots','async'])}
${codeBlock('python', `await app.answer_inline_query(
    inline_query_id,    # str
    results,            # List[InlineQueryResult]
    cache_time=300,
    is_personal=None,
    next_offset=None,
    switch_pm_text=None,
    switch_pm_parameter=None,
)`)}
<h2>Example</h2>
${codeBlock('python', `from ftmgram.types import InlineQueryResultArticle, InputTextMessageContent

@app.on_inline_query()
async def inline(client, query):
    await query.answer([
        InlineQueryResultArticle(
            title="Hello",
            input_message_content=InputTextMessageContent("Hello from inline!"),
        )
    ])`)}`,

// ─────────────────────────────────────────────────────────────
set_bot_commands: () => `
${breadcrumb('Bots', 'set_bot_commands')}
${methodHeader('set_bot_commands', 'Set the bot\'s command list shown in the Telegram command menu.', ['bots','async'])}
${codeBlock('python', `await app.set_bot_commands(
    commands,           # List[BotCommand]
    scope=None,         # BotCommandScope
    language_code=None, # str
)`)}
<h2>Example</h2>
${codeBlock('python', `from ftmgram.types import BotCommand

await app.set_bot_commands([
    BotCommand("start",   "Start the bot"),
    BotCommand("help",    "Show help"),
    BotCommand("ping",    "Check if bot is alive"),
])`)}`,

// ─────────────────────────────────────────────────────────────
get_bot_commands: () => `
${breadcrumb('Bots', 'get_bot_commands')}
${methodHeader('get_bot_commands', 'Get the current list of bot commands.', ['bots','async'])}
${codeBlock('python', `commands = await app.get_bot_commands(
    scope=None,
    language_code=None,
)`)}
${returns('List[types.BotCommand]','The current command list.')}
<h2>Example</h2>
${codeBlock('python', `commands = await app.get_bot_commands()
for cmd in commands:
    print(f"/{cmd.command} — {cmd.description}")`)}`,

// ─────────────────────────────────────────────────────────────
send_invoice: () => `
${breadcrumb('Bots', 'send_invoice')}
${methodHeader('send_invoice', 'Send an invoice for goods or services.', ['bots','async'])}
${codeBlock('python', `await app.send_invoice(
    chat_id,
    title,              # str
    description,        # str
    payload,            # str — bot-defined payload
    currency,           # str — "USD", "INR", "XTR" (Stars)
    prices,             # List[LabeledPrice]
    provider_token="",  # str — empty for Stars
    reply_parameters=None,
    reply_markup=None,
)`)}
<h2>Example</h2>
${codeBlock('python', `from ftmgram.types import LabeledPrice

# Telegram Stars payment
await app.send_invoice(
    chat_id,
    title="Premium Access",
    description="30 days of premium features",
    payload="premium_30d",
    currency="XTR",
    prices=[LabeledPrice("30 Days", 100)]  # 100 Stars
)`)}`,

// ─────────────────────────────────────────────────────────────
answer_pre_checkout_query: () => `
${breadcrumb('Bots', 'answer_pre_checkout_query')}
${methodHeader('answer_pre_checkout_query', 'Confirm or reject a pre-checkout query (finalise payment).', ['bots','async'])}
${codeBlock('python', `await app.answer_pre_checkout_query(
    pre_checkout_query_id,  # str
    ok,                     # bool — True to confirm, False to reject
    error_message=None,     # str — required if ok=False
)`)}
<h2>Example</h2>
${codeBlock('python', `@app.on_pre_checkout_query()
async def pre_checkout(client, query):
    # Validate order here
    await query.answer(ok=True)  # Approve payment`)}`,

// ─────────────────────────────────────────────────────────────
answer_chat_join_request_query: () => `
${breadcrumb('Bots', 'answer_chat_join_request_query')}
${methodHeader('answer_chat_join_request_query', 'Answer a chat join request query from a guard bot (Bot API 10.1).', ['bots','async','new'])}

<div class="note-box"><strong>Bot API 10.1 — New:</strong> Guard bots can now approve, decline, or queue join requests via this method.</div>

${codeBlock('python', `await app.answer_chat_join_request_query(
    query_id,       # int — from ChatJoinRequest.query_id
    result,         # enums.ChatJoinRequestQueryResult
)`)}
${paramsTable([
  { name:'query_id', type:'int', required:true, desc:'The query ID from the ChatJoinRequest update.' },
  { name:'result', type:'enums.ChatJoinRequestQueryResult', required:true, desc:'APPROVE, DECLINE, or QUEUE.' },
])}
<h2>Example</h2>
${codeBlock('python', `from ftmgram import enums

@app.on_chat_join_request()
async def handle_request(client, request):
    if request.query_id:
        # Auto-approve all requests
        await app.answer_chat_join_request_query(
            request.query_id,
            enums.ChatJoinRequestQueryResult.APPROVE
        )`)}`,

// ─────────────────────────────────────────────────────────────
verify_user: () => `
${breadcrumb('Bots', 'verify_user')}
${methodHeader('verify_user', 'Add a verification checkmark to a user (Bot API 10.1).', ['bots','async','new'])}
${codeBlock('python', `await app.verify_user(
    user_id,            # int | str
    custom_description=None,    # str — max 70 chars
)`)}
<h2>Example</h2>
${codeBlock('python', `await app.verify_user(user_id, custom_description="Verified member")`)}`,

// ─────────────────────────────────────────────────────────────
create_bot: () => `
${breadcrumb('Bots', 'create_bot')}
${methodHeader('create_bot', 'Create a new bot account programmatically (users only).', ['users','async'])}
${codeBlock('python', `bot = await app.create_bot(
    first_name,     # str
    username,       # str — must end with "bot"
)`)}
${returns('types.User','The newly created bot user object.')}
<h2>Example</h2>
${codeBlock('python', `new_bot = await app.create_bot("My Awesome Bot", "myawesomebot")
print(new_bot.id, new_bot.username)`)}`,

// ══════════════════════════════════════════════════════════════
// UTILITIES
// ══════════════════════════════════════════════════════════════

start: () => `
${breadcrumb('Utilities', 'start')}
${methodHeader('start', 'Connect to Telegram and start the client. Manages authentication for new sessions.', ['users','bots','async'])}
${codeBlock('python', `await app.start(
    use_qr=False,       # bool — use QR code login
    except_ids=[],      # List[int] — skip if already logged in as these IDs
)`)}
${returns('Client','The started client itself.')}
<h2>Example</h2>
${codeBlock('python', `app = Client("my_account", api_id=12345, api_hash="hash")

async def main():
    await app.start()
    me = await app.get_me()
    print(f"Started as {me.first_name}")
    await app.stop()

asyncio.run(main())`)}`,

// ─────────────────────────────────────────────────────────────
stop: () => `
${breadcrumb('Utilities', 'stop')}
${methodHeader('stop', 'Stop the client — disconnect from Telegram.', ['users','bots','async'])}
${codeBlock('python', `await app.stop(block=True)`)}
<h2>Example</h2>
${codeBlock('python', `await app.start()
# ... do work ...
await app.stop()`)}`,

// ─────────────────────────────────────────────────────────────
run: () => `
${breadcrumb('Utilities', 'run')}
${methodHeader('run', 'Start, run a coroutine, then stop. Convenience method for scripts.', ['users','bots'])}
${codeBlock('python', `app.run(coroutine=None)`)}
<h2>Examples</h2>
<h4>Handler-based bot (runs forever until interrupted)</h4>
${codeBlock('python', `@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello!")

app.run()  # blocks until Ctrl+C`)}

<h4>Single task script</h4>
${codeBlock('python', `async def main():
    async with app:
        await app.send_message("me", "Script ran!")

app.run(main())`)}`,

// ─────────────────────────────────────────────────────────────
idle: () => `
${breadcrumb('Utilities', 'idle')}
${methodHeader('idle', 'Block until one of the stop signals (SIGINT, SIGTERM, SIGABRT) is received. Use in multi-client setups.', ['users','bots','async'])}
${codeBlock('python', `from ftmgram import idle
await idle()`)}
<h2>Example</h2>
${codeBlock('python', `from ftmgram import idle

async def main():
    await app1.start()
    await app2.start()
    await idle()  # wait forever
    await app1.stop()
    await app2.stop()

asyncio.run(main())`)}`,

// ─────────────────────────────────────────────────────────────
add_handler: () => `
${breadcrumb('Utilities', 'add_handler')}
${methodHeader('add_handler', 'Register an update handler programmatically (alternative to decorators).', ['users','bots'])}
${codeBlock('python', `app.add_handler(
    handler,    # Handler — e.g. MessageHandler(...)
    group=0,    # int — handler group, lower runs first
)`)}
<h2>Example</h2>
${codeBlock('python', `from ftmgram import filters
from ftmgram.handlers import MessageHandler

async def my_handler(client, message):
    await message.reply("Handled!")

app.add_handler(MessageHandler(my_handler, filters.text))`)}`,

// ─────────────────────────────────────────────────────────────
export_session_string: () => `
${breadcrumb('Utilities', 'export_session_string')}
${methodHeader('export_session_string', 'Export the current session as a string to restore it later or use in memory.', ['users','bots','async'])}
${codeBlock('python', `session_str = await app.export_session_string()`)}
${returns('str','The session string.')}
<h2>Example</h2>
${codeBlock('python', `async with app:
    session = await app.export_session_string()
    print(session)  # Save this securely!

# Later, restore it:
app2 = Client("restored", api_id=12345, api_hash="hash", session_string=session)
async with app2:
    print(await app2.get_me())`)}

<div class="warn-box"><strong>Warning:</strong> Your session string gives full access to your account. Never share it or commit it to source control.</div>`,

// ══════════════════════════════════════════════════════════════
// HANDLERS
// ══════════════════════════════════════════════════════════════

message_handler: () => `
${breadcrumb('Handlers', 'MessageHandler')}
<div class="method-header">
  <h1>MessageHandler</h1>
  <p>Handle incoming messages in chats, groups, and channels.</p>
  <div class="method-tags"><span class="tag tag-user">👤 Users</span><span class="tag tag-bot">🤖 Bots</span></div>
</div>
<h2>Usage — Decorator</h2>
${codeBlock('python', `from ftmgram import filters

@app.on_message(filters.text & filters.private)
async def handle_text(client, message):
    print(message.text)
    await message.reply(f"You said: {message.text}")`)}

<h2>Usage — Programmatic</h2>
${codeBlock('python', `from ftmgram.handlers import MessageHandler
from ftmgram import filters

async def handle(client, message):
    await message.reply("Got your message!")

app.add_handler(MessageHandler(handle, filters.text))`)}

<h2>Common Filters</h2>
${codeBlock('python', `filters.text          # Text messages only
filters.photo         # Photo messages
filters.video         # Video messages
filters.document      # Document messages
filters.audio         # Audio messages
filters.sticker       # Sticker messages
filters.private       # Private chats only
filters.group         # Group chats only
filters.channel       # Channel posts only
filters.command("start")  # /start command
filters.regex(r"hello")   # Messages matching regex
filters.user(user_id)     # From specific user
filters.chat(chat_id)     # From specific chat
~filters.bot          # Not from a bot`)}

<h2>Message object key attributes</h2>
${codeBlock('python', `message.id            # int — message ID
message.text          # str — text content
message.caption       # str — media caption
message.from_user     # User — sender
message.chat          # Chat — where it was sent
message.photo         # Photo object (if photo)
message.video         # Video object (if video)
message.document      # Document object
message.reply_to_message  # Replied-to message
message.date          # datetime of send`)}`,

// ─────────────────────────────────────────────────────────────
callback_query_handler: () => `
${breadcrumb('Handlers', 'CallbackQueryHandler')}
<div class="method-header">
  <h1>CallbackQueryHandler</h1>
  <p>Handle callback queries from inline keyboard button presses.</p>
  <div class="method-tags"><span class="tag tag-bot">🤖 Bots</span></div>
</div>
<h2>Decorator</h2>
${codeBlock('python', `@app.on_callback_query(filters.regex("^btn_"))
async def handle_btn(client, query):
    await query.answer(f"Clicked: {query.data}")
    await query.message.edit_text(f"You pressed: {query.data}")`)}

<h2>Programmatic</h2>
${codeBlock('python', `from ftmgram.handlers import CallbackQueryHandler

async def cb_handler(client, query):
    await query.answer("Done!")

app.add_handler(CallbackQueryHandler(cb_handler))`)}

<h2>Query object attributes</h2>
${codeBlock('python', `query.id          # str — query ID
query.from_user   # User — who pressed
query.message     # Message — the message with the button
query.data        # str — callback data
query.chat_instance  # str`)}`,

// ─────────────────────────────────────────────────────────────
inline_query_handler: () => `
${breadcrumb('Handlers', 'InlineQueryHandler')}
<div class="method-header">
  <h1>InlineQueryHandler</h1>
  <p>Handle inline queries (when users type @yourbot in any chat).</p>
  <div class="method-tags"><span class="tag tag-bot">🤖 Bots</span></div>
</div>
<h2>Example</h2>
${codeBlock('python', `from ftmgram.types import InlineQueryResultArticle, InputTextMessageContent

@app.on_inline_query()
async def inline(client, query):
    results = [
        InlineQueryResultArticle(
            title=f"Result for: {query.query}",
            input_message_content=InputTextMessageContent(
                f"You searched: {query.query}"
            ),
            description="Click to send"
        )
    ]
    await query.answer(results, cache_time=1)`)}`,

// ─────────────────────────────────────────────────────────────
edited_message_handler: () => `
${breadcrumb('Handlers', 'EditedMessageHandler')}
<div class="method-header">
  <h1>EditedMessageHandler</h1>
  <p>Handle edited messages.</p>
  <div class="method-tags"><span class="tag tag-user">👤 Users</span><span class="tag tag-bot">🤖 Bots</span></div>
</div>
<h2>Example</h2>
${codeBlock('python', `@app.on_edited_message(filters.text)
async def edited(client, message):
    print(f"Message {message.id} was edited to: {message.text}")`)}`,

// ─────────────────────────────────────────────────────────────
chat_member_updated_handler: () => `
${breadcrumb('Handlers', 'ChatMemberUpdatedHandler')}
<div class="method-header">
  <h1>ChatMemberUpdatedHandler</h1>
  <p>Handle chat member updates — joins, leaves, promotions, bans.</p>
  <div class="method-tags"><span class="tag tag-user">👤 Users</span><span class="tag tag-bot">🤖 Bots</span></div>
</div>
<h2>Example</h2>
${codeBlock('python', `from ftmgram import enums

@app.on_chat_member_updated()
async def member_update(client, update):
    if update.new_chat_member.status == enums.ChatMemberStatus.MEMBER:
        await app.send_message(
            update.chat.id,
            f"Welcome {update.new_chat_member.user.first_name}! 👋"
        )`)}`,

// ─────────────────────────────────────────────────────────────
chat_join_request_handler: () => `
${breadcrumb('Handlers', 'ChatJoinRequestHandler')}
<div class="method-header">
  <h1>ChatJoinRequestHandler</h1>
  <p>Handle join requests for groups and channels with approval required.</p>
  <div class="method-tags"><span class="tag tag-user">👤 Users</span><span class="tag tag-bot">🤖 Bots</span></div>
</div>
<h2>Example</h2>
${codeBlock('python', `@app.on_chat_join_request()
async def join_req(client, request):
    # Auto approve all
    await app.approve_chat_join_request(request.chat.id, request.from_user.id)
    await app.send_message(
        request.from_user.id,
        "Your join request was approved! ✅"
    )`)}`,

// ─────────────────────────────────────────────────────────────
poll_handler: () => `
${breadcrumb('Handlers', 'PollHandler')}
<div class="method-header">
  <h1>PollHandler</h1>
  <p>Handle poll updates (new votes, poll closed, etc.).</p>
  <div class="method-tags"><span class="tag tag-bot">🤖 Bots</span></div>
</div>
<h2>Example</h2>
${codeBlock('python', `@app.on_poll()
async def poll_update(client, poll):
    print(f"Poll: {poll.question}")
    for opt in poll.options:
        print(f"  {opt.text}: {opt.voter_count} votes")`)}`,

// ─────────────────────────────────────────────────────────────
story_handler: () => `
${breadcrumb('Handlers', 'StoryHandler')}
<div class="method-header">
  <h1>StoryHandler</h1>
  <p>Handle new stories from contacts or channels you follow.</p>
  <div class="method-tags"><span class="tag tag-user">👤 Users</span></div>
</div>
<h2>Example</h2>
${codeBlock('python', `@app.on_story()
async def on_story(client, story):
    print(f"New story from {story.from_user.first_name}")`)}`,

// ─────────────────────────────────────────────────────────────
error_handler: () => `
${breadcrumb('Handlers', 'ErrorHandler')}
<div class="method-header">
  <h1>ErrorHandler</h1>
  <p>Catch and handle exceptions raised inside other handlers.</p>
  <div class="method-tags"><span class="tag tag-user">👤 Users</span><span class="tag tag-bot">🤖 Bots</span></div>
</div>
<h2>Example</h2>
${codeBlock('python', `@app.on_error()
async def error_handler(client, error):
    print(f"Handler error: {type(error).__name__}: {error}")`)}`,

// ─────────────────────────────────────────────────────────────
raw_update_handler: () => `
${breadcrumb('Handlers', 'RawUpdateHandler')}
<div class="method-header">
  <h1>RawUpdateHandler</h1>
  <p>Receive all raw MTProto updates before they are processed. For advanced use cases.</p>
  <div class="method-tags"><span class="tag tag-user">👤 Users</span><span class="tag tag-bot">🤖 Bots</span></div>
</div>
<h2>Example</h2>
${codeBlock('python', `from ftmgram.handlers import RawUpdateHandler

async def raw(client, update, users, chats):
    print(type(update).__name__, update)

app.add_handler(RawUpdateHandler(raw))`)}`,

// ══════════════════════════════════════════════════════════════
// ENUMS
// ══════════════════════════════════════════════════════════════

enum_ChatType: () => enumPage('ChatType','Enums',
  'Chat type enumeration used in <code>types.Chat</code>.',
  [
    { key:'PRIVATE',    desc:'Chat is a private one-on-one conversation with a regular user.' },
    { key:'BOT',        desc:'Chat is a private conversation with a bot.' },
    { key:'GROUP',      desc:'Chat is a basic group (up to 200 members).' },
    { key:'SUPERGROUP', desc:'Chat is a supergroup (up to 200,000 members).' },
    { key:'CHANNEL',    desc:'Chat is a broadcast channel.' },
    { key:'FORUM',      desc:'Chat is a forum (supergroup with topics enabled).' },
    { key:'DIRECT',     desc:'Chat is a direct message channel (channel DMs).' },
  ]),

enum_ParseMode: () => enumPage('ParseMode','Enums',
  'Controls how text is parsed when sending messages.',
  [
    { key:'DEFAULT',  desc:'Use both Markdown and HTML parsing (default behaviour).' },
    { key:'HTML',     desc:'Parse text as HTML — use &lt;b&gt;, &lt;i&gt;, &lt;code&gt;, &lt;a href&gt; etc.' },
    { key:'MARKDOWN', desc:'Parse text as Markdown — use **bold**, __italic__, `code`, [link](url).' },
    { key:'DISABLED', desc:'No parsing — treat the text as plain.' },
  ]),

enum_MessageMediaType: () => enumPage('MessageMediaType','Enums',
  'Media type of the message. Accessible via <code>message.media</code>.',
  [
    { key:'AUDIO',       desc:'Message contains an audio file.' },
    { key:'DOCUMENT',    desc:'Message contains a generic document.' },
    { key:'PHOTO',       desc:'Message contains a photo.' },
    { key:'LIVE_PHOTO',  desc:'Message contains a live photo.' },
    { key:'STICKER',     desc:'Message contains a sticker.' },
    { key:'VIDEO',       desc:'Message contains a video.' },
    { key:'ANIMATION',   desc:'Message contains a GIF or silent video animation.' },
    { key:'VOICE',       desc:'Message contains a voice note.' },
    { key:'VIDEO_NOTE',  desc:'Message contains a video note (circle).' },
    { key:'CONTACT',     desc:'Message contains a contact.' },
    { key:'LOCATION',    desc:'Message contains a location.' },
    { key:'VENUE',       desc:'Message contains a venue.' },
    { key:'POLL',        desc:'Message contains a poll.' },
    { key:'WEB_PAGE',    desc:'Message contains a web page preview.' },
    { key:'DICE',        desc:'Message contains an animated dice.' },
    { key:'GAME',        desc:'Message contains a game.' },
    { key:'GIVEAWAY',    desc:'Message contains a giveaway.' },
    { key:'CHECKLIST',   desc:'✨ New — Message contains a checklist (Bot API 10.1).' },
    { key:'LINK',        desc:'✨ New — Message contains a link media (Bot API 10.1).' },
    { key:'UNSUPPORTED', desc:'Media type not supported in this version.' },
  ]),

enum_ChatMemberStatus: () => enumPage('ChatMemberStatus','Enums',
  'Status of a member in a chat. Used in <code>types.ChatMember</code>.',
  [
    { key:'OWNER',         desc:'The chat creator.' },
    { key:'ADMINISTRATOR', desc:'An administrator with custom privileges.' },
    { key:'MEMBER',        desc:'A regular chat member.' },
    { key:'RESTRICTED',    desc:'A restricted (but not banned) member.' },
    { key:'LEFT',          desc:'A user who left or was removed.' },
    { key:'BANNED',        desc:'A banned/kicked user.' },
  ]),

enum_ChatAction: () => enumPage('ChatAction','Enums',
  'Chat actions for <code>send_chat_action()</code>. Tell users what the bot/user is doing.',
  [
    { key:'TYPING',            desc:'Typing a text message.' },
    { key:'UPLOAD_PHOTO',      desc:'Uploading a photo.' },
    { key:'RECORD_VIDEO',      desc:'Recording a video.' },
    { key:'UPLOAD_VIDEO',      desc:'Uploading a video.' },
    { key:'RECORD_AUDIO',      desc:'Recording an audio message.' },
    { key:'UPLOAD_AUDIO',      desc:'Uploading an audio file.' },
    { key:'UPLOAD_DOCUMENT',   desc:'Uploading a document.' },
    { key:'FIND_LOCATION',     desc:'Selecting a location.' },
    { key:'RECORD_VIDEO_NOTE', desc:'Recording a video note.' },
    { key:'UPLOAD_VIDEO_NOTE', desc:'Uploading a video note.' },
    { key:'PLAYING',           desc:'Playing a game.' },
    { key:'CHOOSE_CONTACT',    desc:'Choosing a contact.' },
    { key:'SPEAKING',          desc:'Speaking in a group voice call.' },
    { key:'CHOOSE_STICKER',    desc:'Choosing a sticker.' },
    { key:'CANCEL',            desc:'Cancel the current chat action.' },
  ]),

enum_MessageEntityType: () => enumPage('MessageEntityType','Enums',
  'Type of a text entity inside a message. Used in <code>types.MessageEntity</code>.',
  [
    { key:'MENTION',      desc:'@username mention.' },
    { key:'HASHTAG',      desc:'#hashtag.' },
    { key:'CASHTAG',      desc:'$USD cashtag.' },
    { key:'BOT_COMMAND',  desc:'/command bot command.' },
    { key:'URL',          desc:'Plain URL.' },
    { key:'EMAIL',        desc:'Email address.' },
    { key:'PHONE_NUMBER', desc:'Phone number.' },
    { key:'BOLD',         desc:'Bold text.' },
    { key:'ITALIC',       desc:'Italic text.' },
    { key:'UNDERLINE',    desc:'Underlined text.' },
    { key:'STRIKETHROUGH',desc:'Strikethrough text.' },
    { key:'SPOILER',      desc:'Spoiler text (hidden until tapped).' },
    { key:'CODE',         desc:'Monospace inline code.' },
    { key:'PRE',          desc:'Monospace code block.' },
    { key:'BLOCKQUOTE',   desc:'Block quote.' },
    { key:'TEXT_LINK',    desc:'Clickable text with a URL.' },
    { key:'TEXT_MENTION', desc:'Mention for users without a username.' },
  ]),

enum_SentCodeType: () => enumPage('SentCodeType','Enums',
  'Type of authentication code sent during login.',
  [
    { key:'APP',         desc:'Code delivered via Telegram app notification.' },
    { key:'SMS',         desc:'Code sent as an SMS.' },
    { key:'CALL',        desc:'Code delivered via a phone call.' },
    { key:'FLASH_CALL',  desc:'Code via a flash call (the number itself is the code).' },
    { key:'FRAGMENT_SMS',desc:'Code via Fragment SMS.' },
    { key:'EMAIL_CODE',  desc:'Code sent to email.' },
    { key:'FIREBASE_SMS',desc:'Code via Firebase SMS.' },
  ]),

enum_MessagesFilter: () => enumPage('MessagesFilter','Enums',
  'Filter for <code>search_messages()</code> to find specific media types.',
  [
    { key:'EMPTY',         desc:'No filter — search all messages.' },
    { key:'PHOTO',         desc:'Photos only.' },
    { key:'VIDEO',         desc:'Videos only.' },
    { key:'PHOTO_VIDEO',   desc:'Both photos and videos.' },
    { key:'DOCUMENT',      desc:'Documents only.' },
    { key:'URL',           desc:'Messages containing URLs.' },
    { key:'ANIMATION',     desc:'GIF/animations only.' },
    { key:'VOICE_NOTE',    desc:'Voice notes only.' },
    { key:'AUDIO',         desc:'Audio files only.' },
    { key:'VIDEO_NOTE',    desc:'Video notes only.' },
    { key:'CHAT_PHOTO',    desc:'Chat photo changes.' },
    { key:'PHONE_CALL',    desc:'Phone calls.' },
    { key:'MENTION',       desc:'Messages where you were mentioned.' },
    { key:'PINNED',        desc:'Pinned messages.' },
  ]),

enum_ChatMembersFilter: () => enumPage('ChatMembersFilter','Enums',
  'Filter for <code>get_chat_members()</code>.',
  [
    { key:'SEARCH',         desc:'Search members by name.' },
    { key:'BANNED',         desc:'Banned (kicked) members.' },
    { key:'RESTRICTED',     desc:'Restricted members.' },
    { key:'BOTS',           desc:'Bots only.' },
    { key:'RECENT',         desc:'Recently active members.' },
    { key:'ADMINISTRATORS', desc:'Admins only.' },
  ]),

enum_StickerType: () => enumPage('StickerType','Enums',
  'Sticker format type.',
  [
    { key:'REGULAR',   desc:'Regular static or animated sticker (.webp or .tgs).' },
    { key:'MASK',      desc:'Mask sticker that attaches to faces.' },
    { key:'CUSTOM_EMOJI', desc:'Custom emoji sticker.' },
  ]),

enum_ButtonStyle: () => enumPage('ButtonStyle','Enums',
  'Visual style for keyboard buttons.',
  [
    { key:'DEFAULT', desc:'Default neutral button style.' },
    { key:'PRIMARY', desc:'Dark blue primary action button.' },
    { key:'DANGER',  desc:'Red destructive action button.' },
    { key:'SUCCESS', desc:'Green confirmation button.' },
  ]),

enum_ChatJoinType: () => enumPage('ChatJoinType','Enums',
  'How a user joined a chat — used in the NEW_CHAT_MEMBERS service message.',
  [
    { key:'BY_ADD',     desc:'Member was added by another user.' },
    { key:'BY_LINK',    desc:'Member joined via an invite link.' },
    { key:'BY_REQUEST', desc:'Member was accepted by an admin after requesting.' },
  ]),

enum_GiftType: () => enumPage('GiftType','Enums',
  'Type of a Telegram gift.',
  [
    { key:'REGULAR',  desc:'A standard regular gift.' },
    { key:'UPGRADED', desc:'An upgraded (NFT-style) collectible gift.' },
  ]),

enum_PollType: () => enumPage('PollType','Enums',
  'Poll type used when creating polls with <code>send_poll()</code>.',
  [
    { key:'REGULAR', desc:'A standard poll where voters can see all results.' },
    { key:'QUIZ',    desc:'A quiz with one correct answer and optional explanation.' },
  ]),

enum_UserStatus: () => enumPage('UserStatus','Enums',
  'Online presence status of a user.',
  [
    { key:'ONLINE',    desc:'User is currently online.' },
    { key:'OFFLINE',   desc:'User is offline. Last seen time is available.' },
    { key:'RECENTLY',  desc:'Was online recently (within last 1–2 days).' },
    { key:'LAST_WEEK', desc:'Was online last week.' },
    { key:'LAST_MONTH',desc:'Was online last month.' },
    { key:'LONG_AGO',  desc:'Was online a long time ago.' },
  ]),

enum_BlockList: () => enumPage('BlockList','Enums',
  'Block list type for <code>block_user()</code>.',
  [
    { key:'MAIN',   desc:'Main block list — prevents messages, status, photos, stories and other interactions.' },
    { key:'STORIES',desc:'Stories block list — only hides your stories from this user.' },
  ]),

enum_ChatEventAction: () => enumPage('ChatEventAction','Enums',
  'Type of event in the admin event log (<code>get_chat_event_log</code>).',
  [
    { key:'DESCRIPTION_CHANGED',      desc:'Chat description was changed.' },
    { key:'HISTORY_TTL_CHANGED',      desc:'History TTL (auto-delete timer) changed.' },
    { key:'LINKED_CHAT_CHANGED',      desc:'Linked chat changed.' },
    { key:'PHOTO_CHANGED',            desc:'Chat photo changed.' },
    { key:'TITLE_CHANGED',            desc:'Chat title changed.' },
    { key:'USERNAME_CHANGED',         desc:'Chat username changed.' },
    { key:'CHAT_PERMISSIONS_CHANGED', desc:'Default chat permissions changed.' },
    { key:'MESSAGE_DELETED',          desc:'A message was deleted by an admin.' },
    { key:'MESSAGE_EDITED',           desc:'A message was edited by an admin.' },
    { key:'INVITE_LINK_EDITED',       desc:'An invite link was edited.' },
    { key:'INVITE_LINK_REVOKED',      desc:'An invite link was revoked.' },
    { key:'MEMBER_INVITED',           desc:'A member was invited by someone.' },
    { key:'MEMBER_JOINED',            desc:'A member joined on their own.' },
  ]),

enum_FolderColor: () => enumPage('FolderColor','Enums',
  'Color tag for chat folders.',
  [
    { key:'NO_COLOR', desc:'No color tag.' },
    { key:'RED',      desc:'Red color.' },
    { key:'ORANGE',   desc:'Orange color.' },
    { key:'VIOLET',   desc:'Violet/purple color.' },
    { key:'GREEN',    desc:'Green color.' },
    { key:'CYAN',     desc:'Cyan color.' },
    { key:'BLUE',     desc:'Blue color.' },
    { key:'PINK',     desc:'Pink color.' },
  ]),

enum_MediaAreaType: () => enumPage('MediaAreaType','Enums',
  'Type of an interactive area in a story.',
  [
    { key:'POST',     desc:'Links to a channel post.' },
    { key:'LOCATION', desc:'Geographic location pin.' },
    { key:'REACTION', desc:'Reaction suggestion area.' },
    { key:'URL',      desc:'Clickable URL area.' },
    { key:'VENUE',    desc:'Venue location.' },
    { key:'WEATHER',  desc:'Weather widget.' },
    { key:'GIFT',     desc:'Star gift display area.' },
  ]),

enum_PrivacyKey: () => enumPage('PrivacyKey','Enums',
  'Privacy setting keys for <code>get_privacy()</code> and <code>set_privacy()</code>.',
  [
    { key:'STATUS',          desc:'Who can see your last seen/online status.' },
    { key:'CHAT_INVITE',     desc:'Who can add you to groups/channels.' },
    { key:'PHONE_CALL',      desc:'Who can call you.' },
    { key:'PHONE_P2P',       desc:'Who can make peer-to-peer calls with you.' },
    { key:'FORWARDS',        desc:'Whether forwarded messages show your name.' },
    { key:'PROFILE_PHOTO',   desc:'Who can see your profile photo.' },
    { key:'PHONE_NUMBER',    desc:'Who can see your phone number.' },
    { key:'ADDED_BY_PHONE',  desc:'Who can find you by phone number.' },
    { key:'VOICE_MESSAGES',  desc:'Who can send you voice messages.' },
    { key:'BIO',             desc:'Who can see your bio.' },
  ]),

}; // end PAGES
