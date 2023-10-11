## Table of Contents

Join the [AstroDX discord](https://discord.gg/6fpETgpvjZ) and ask in #general or the help forum
if your question isn't listed.

- [Installation](#installation)
  - [iOS](#ios)
  - [Android](#android)
- [Migration](#migration)
  - [Transferring from AstroDX 1.1/1.9 to AstroDX 2.0](#transferring-from-astrodx-1119-to-astrodx-20)
- [Levels](#levels)
  - [Where do I download levels?](#where-do-i-download-levels)
  - [How do I import levels?](#how-do-i-import-levels)
  - [Downloading from Google Drive on mobile devices](#downloading-from-google-drive)
  - [Why do FESTiVAL charts not play properly?](#why-do-festival-charts-not-play-properly)
  - [Can I delete pv.mp4?](#can-i-delete-pvmp4)
  - [All the songs are early/late?](#all-the-songs-are-earlylate)
  - [I upgraded and the levels disappeared?](#i-upgraded-and-the-levels-disappeared)
- [Settings](#settings)
  - [How do I edit settings?](#how-do-i-edit-settings)

## Installation
### iOS
<!--
full = "https://img.shields.io/badge/${group_name}-full-red"
closed = "https://img.shields.io/badge/${group_name}-closed-yellow"
open = "https://img.shields.io/badge/${group_name}-open-green"
 -->
Join the public TestFlight (click on one of the badges): [![AstroDX Group A TestFlight status](https://img.shields.io/badge/Group%20A-full-red)](https://testflight.apple.com/join/rACTLjPL) [![AstroDX Group B TestFlight status](https://img.shields.io/badge/Group%20B-full-red)](https://testflight.apple.com/join/ocj3yptn).

Due to AstroDX's popularity, these groups are very often full. However, inactive testers
are periodically cleared, so regularly watch out for open spots!

### Android
Download the latest APK from the [AstroDX releases page](https://github.com/2394425147/maipaddx/releases) ![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/2394425147/maipaddx?include_prereleases).

## Migration
### Transferring from AstroDX 1.1/1.9 to AstroDX 2.0
1. Backup your `maipaddx`/`com.Reflektone.MaipadDX` folder to somewhere else
2. Install AstroDX 2.0 and open the game at least once
3. Migrate your levels to `com.Reflektone.AstroDX/files/levels` (for iOS, rename `local` to `levels` is enough)
4. Copy `chart-meta.fufu` into `com.Reflektone.AstroDX/files`
5. Start the game and your scores *should* be migrated.

## Levels
### Where do I download levels?
Join the [AstroDX discord](https://discord.gg/6fpETgpvjZ) for level sharing.

There are also other sources on the Internet, explore and find out!

### How do I import levels?
Place them under `AstroDX/levels` (iOS) or `Android/data/com.Reflektone.AstroDX/files/levels` (Android)
according to this structure:

```
AstroDX
└───[1] levels
    ├───[2] song
    └───[3] category
        └───[2] song
            ├─── maidata.txt
            ├─── track.mp3
            ├─── bg.png
            └─── pv.mp4

```
1. All levels and categories should be placed under this folder.
2. An AstroDX level. You can put it directly under `levels`, or group levels into a `category` (3) folder.
A valid level must consist of at least `maidata.txt` and `track.mp3`.

For (2) and (3), the names don't have to be `song` and `category`, you can name them whatever you like!

### Downloading from Google Drive on mobile devices
You will need to use your device's web browser and enable "Request Desktop Website", as downloading from the Google
Drive app is not supported.
  - Chrome: Tap on 3 dots (•••) on top right, then tick on "Desktop site".
  - Safari: Tap on "Aa"/"大小" on the left of the address bar, then select "Request Desktop Website".

### Why do FESTiVAL charts not play properly?
FESTiVAL charts are only supported since `v2.0.0.beta.pre.83`, so you need to be on that version to play them.

Some charters also support older versions of AstroDX/MaipadDX by providing a "fakefes" chart (for example, slides
chained together using tapless slides) and naming it `maidata_dx.txt`. Due to a bug in AstroDX, `maidata_dx.txt`
will be prioritized over `maidata.txt`, effectively playing the fakefes version instead of the original. Check the
song folder for `maidata_dx.txt` and delete it if it exists.

### Can I delete pv.mp4?
Yes.

### All the songs are early/late?
Adjust offset in settings.

### I upgraded and the levels disappeared?
Rename `AstroDX/local` to `AstroDX/levels`.

## Settings
### How do I edit settings?
Settings menu is not yet implemented, so you will need to edit `settings.json` manually:
- iOS: Files -> `AstroDX/settings.json`
- Android: `Android/data/com.Reflektone.AstroDX/files/settings.json`

I recommend using a dedicated JSON editor such as [Jayson](https://apps.apple.com/us/app/jayson/id1447750768) (iOS)
and [JSON Genie](https://play.google.com/store/apps/details?id=com.tuyware.jsongenie&hl=en&gl=US) (Android) to
prevent common mistakes when manually editing.

For detail on what the setting keys mean, check this [gist](https://gist.github.com/beerpiss/653d5a64f4b75c6910f5ddf222daf8b4).


