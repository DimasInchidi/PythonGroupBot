It's a Telegram bot for the @python group maintained by the admins.

TODO/Changelog:
- [x] Auto-lang detection.
- [x] Ignore special texts that are supposed to be in English.
- [x] `new()` is now able to make new keys.
- [x] NEW FUNC: `ignore()`. Add new texts to ignore to `ignore.json`
- [x] NEW FUNC: `ignorelist()`. Get a list of the stuff that get ignored.
- [x] Switched to `TinyDB` (it's meh.)
- [x] Button to translate the "I've detected..." message to the detected language.
- [x] A function that translates a text. (not used yet)
- [ ] Meta questions detector.
- [ ] Resend messages (then delete the old ones) with code that aren't formatted in Markdown. (Fucking annoys me)


# RUNNING TEST:
to run test, run `python -m unittest -v tests` from /src/