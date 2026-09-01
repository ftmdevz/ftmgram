==============
Release Notes
==============

Release notes for FTMGram releases will describe what's new in each version, and will also make you aware of any backwards-incompatible changes made in that version.

.. admonition :: A Word of Warning
    :class: tip
    
    We merge changes made to few of ftmgram forks plus changes made by us to this repository. All the features are just customized feature mostly for personal use; there is no guarantee in them being stable, **USE AT YOUR OWN RISK**.


When upgrading to a new version of FTMGram, you will need to check all the changes in order to find incompatible code in your application, but also to take advantage of new features and improvements.

This page lists all the documented changes of this fork,
in reverse chronological order. You should read this when upgrading
to this fork to know where your code can break, and where
it can take advantage of new goodies!

`For a more detailed description, please check the commits. <https://github.com/TelegramPlayGround/FTMGram/commits/dev/>`__

If you found any issue or have any suggestions, feel free to make `an issue <https://github.com/TelegramPlayGround/FTMGram/issues>`__ on github.

.. admonition :: Breaking Changes in this Fork
    :class: tip

    - In :meth:`~ftmgram.Client.copy_message`, ``ValueError`` is raised instead of ``logging`` it.
    - In :meth:`~ftmgram.Client.download_media`, if the message is a :obj:`~ftmgram.types.PaidMediaInfo` with more than one ``paid_media`` **and** ``idx`` was not specified, then a list of paths or binary file-like objects is returned.
    - PR `#115 <https://github.com/TelegramPlayGround/FTMGram/pull/115>`_ This `change <https://github.com/ftmgram/ftmgram/pull/966#issuecomment-1108858881>`_ breaks some usages with offset-naive and offset-aware datetimes.
    - PR from upstream `#1411 <https://github.com/ftmgram/ftmgram/pull/1411>`_: Rename some of the attributes of :obj:`~ftmgram.enums.MessagesFilter` for consistency.
    - If you relied on internal types like ``import ftmgram.file_id`` OR ``import ftmgram.utils``, Then read this full document to know where `else <https://t.me/FTMGramChat/42497>`_ your code will break.
    - :obj:`~ftmgram.types.InlineKeyboardButton` only accepts keyword arguments instead of positional arguments.


.. toctree::
    :titlesonly:
    :reversed:

    Previous Changes <https://web.archive.org/web/20241127113824/https://docs.ftmgram.org/releases/>
    v2.1.18
    v2.1.19
    v2.1.20
    v2.1.21
    v2.1.22
    v2.1.23
    v2.1.25
    v2.1.26
    v2.1.27
    v2.1.28
    v2.1.29
    v2.1.30
    v2.1.31
    v2.1.32.1
    v2.1.32.2
    v2.1.32.3
    v2.1.32.4
    v2.1.32.6
    v2.1.32.7
    v2.1.32.8
    v2.1.32.9
    v2.1.32.10
    v2.1.32.11
    v2.1.32.12
    v2.1.32.13
    v2.1.32.14
    v2.1.32.15
    v2.1.33.1
    v2.1.33.2
    v2.1.33.3
    v2.1.33.4
    v2.1.33.7
    v2.1.33.8
    v2.1.33.9
    v2.1.33.10
    v2.1.33.11
    v2.1.33.12
    v2.1.33.13
    v2.1.34
    v2.1.35
    v2.1.36
    v2.1.37
    v2.2.1
    v2.2.2
    v2.2.4
    v2.2.5
    v2.2.6
    v2.2.7
    v2.2.8
    v2.2.9
    v2.2.10
    v2.2.11
    v2.2.12
    v2.2.13
    v2.2.14
    v2.2.15
    v2.2.16
    v2.2.17
    v2.2.18
    v2.2.21
    v2.2.22
    v2.2.23
    v2.2.24
    changes-in-this-fork
