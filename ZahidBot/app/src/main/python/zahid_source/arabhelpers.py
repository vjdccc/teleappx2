try:
    import io
except Exception:
    pass
try:
    import os
except Exception:
    pass

try:
    from PIL import Image, ImageDraw, ImageOps
except Exception:
    pass


def convert_toimage(image, filename=None):
    filename = filename or os.path.join("./temp/", "temp.jpg")
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(filename, "jpeg")
    os.remove(image)
    return filename


def convert_tosticker(response, filename=None):
    filename = filename or os.path.join("./temp/", "temp.webp")
    image = Image.open(response)
    if image.mode != "RGB":
        image.convert("RGB")
    image.save(filename, "webp")
    os.remove(response)
    return filename


# http://effbot.org/imagingbook/imageops.html
# https://stackoverflow.com/questions/2498875/how-to-invert-colors-of-image-with-pil-python-imaging/38378828


async def invert_colors(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = ImageOps.invert(image)
    inverted_image.save(endname)


async def flip_image(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = ImageOps.flip(image)
    inverted_image.save(endname)


async def grayscale(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = ImageOps.grayscale(image)
    inverted_image.save(endname)


async def mirror_file(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = ImageOps.mirror(image)
    inverted_image.save(endname)


async def solarize(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = ImageOps.solarize(image, threshold=128)
    inverted_image.save(endname)


async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = ImageOps.crop(image, border=x)
    inverted_image.save(endname)


async def crop_and_divide(img):
    (width, height) = img.size
    rows = 5
    columns = 5
    scale_width = width // columns
    scale_height = height // rows
    if (scale_width * columns, scale_height * rows) != (width, height):
        img = img.resize((scale_width * columns, scale_height * rows))
    (new_width, new_height) = (0, 0)
    media = []
    for _ in range(1, rows + 1):
        for o in range(1, columns + 1):
            mimg = img.crop(
                (
                    new_width,
                    new_height,
                    new_width + scale_width,
                    new_height + scale_height,
                )
            )
            mimg = mimg.resize((512, 512))
            image = io.BytesIO()
            image.name = "zahid.png"
            mimg.save(image, "PNG")
            media.append(image.getvalue())
            new_width += scale_width
        new_width = 0
        new_height += scale_height
    return media


def cirsle(im, x, y, r, fill):
    x += r // 2
    y += r // 2
    draw = ImageDraw.Draw(im)
    draw.ellipse((x - r, y - r, x + r, y + r), fill)
    return im


async def dotify(image, pix, mode):
    count = 24
    im_ = Image.open(image)
    if im_.mode == "RGBA":
        temp = Image.new("RGB", im_.size, "#000")
        temp.paste(im_, (0, 0), im_)
        im_ = temp
    im = im_.convert("L")
    im_ = im if mode else im_
    [_.thumbnail((pix, pix)) for _ in [im, im_]]
    w, h = im.size
    img = Image.new(im_.mode, (w * count + (count // 2), h * count + (count // 2)), 0)
    ImageDraw.Draw(img)
    _x = _y = count // 2
    for x in range(w):
        for y in range(h):
            r = im.getpixel((x, y))
            fill = im_.getpixel((x, y))
            cirsle(img, _x, _y, r // count, fill)
            _y += count
        _x += count
        _y = count // 2
    out = io.BytesIO()
    out.name = "out.png"
    img.save(out)
    out.seek(0)
    return out

try:
    import requests
except Exception:
    pass
try:
    from PIL import Image, ImageDraw, ImageFont
except Exception:
    pass


async def fakegs(search, result):
    imgurl = "https://i.imgur.com/wNFr5X2.jpg"
    with open("./temp/temp.jpg", "wb") as f:
        f.write(requests.get(imgurl).content)
    img = Image.open("./temp/temp.jpg")
    drawing = ImageDraw.Draw(img)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font1 = ImageFont.truetype("zahid/helpers/styles/ProductSans-BoldItalic.ttf", 20)
    font2 = ImageFont.truetype("zahid/helpers/styles/ProductSans-Light.ttf", 23)
    drawing.text((450, 258), result, fill=blue, font=font1)
    drawing.text((270, 37), search, fill=black, font=font2)
    img.save("./temp/temp.jpg")
    return "./temp/temp.jpg"


async def trumptweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    ).json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"


async def changemymind(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}"
    ).json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def kannagen(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=kannagen&text={text}"
    ).json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"


async def moditweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=narendramodi"
    ).json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"


async def tweets(text1, text2):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text1}&username={text2}"
    ).json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"


async def iphonex(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={text}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def baguette(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=baguette&url={text}"
    ).json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def threats(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=threats&url={text}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def lolice(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=lolice&url={text}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def trash(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=trash&url={text}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def awooify(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=awooify&url={text}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def trap(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trap&name={text1}&author={text2}&image={text3}"
    ).json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def phcomment(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=phcomment&image={text1}&text={text2}&username={text3}"
    ).json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"

try:
    import logging
except Exception:
    pass
try:
    import random
except Exception:
    pass

try:
    from moviepy.editor import VideoFileClip
except Exception:
    pass
try:
    from PIL import Image, ImageOps
except Exception:
    pass


LOGS = logging.getLogger(__name__)


async def vid_to_gif(inputfile, outputfile, speed=None, starttime=None, endtime=None):
    try:
        clip = VideoFileClip(inputfile)
        if starttime is not None and endtime is not None:
            clip = clip.subclip(int(starttime), int(endtime))
        if speed is not None:
            clip = clip.speedx(float(speed))
        clip.write_gif(outputfile, logger=None)
        return outputfile
    except Exception as e:
        LOGS.error(e)
        return None


async def r_frames(image, w, h, outframes):
    for i in range(1, w, w // 30):
        img1 = img2 = image.copy()
        temp = Image.new("RGB", (w, h))
        img1 = img1.resize((i, h))
        img2 = img2.resize((w - i, h))
        temp.paste(img1, (0, 0))
        temp.paste(img2, (i, 0))
        outframes.append(temp)
    return outframes


async def l_frames(image, w, h, outframes):
    for i in range(1, w, w // 30):
        img1 = img2 = image.copy()
        temp = Image.new("RGB", (w, h))
        img1 = ImageOps.mirror(img1.resize((i, h)))
        img2 = ImageOps.mirror(img2.resize((w - i, h)))
        temp.paste(img1, (0, 0))
        temp.paste(img2, (i, 0))
        temp = ImageOps.mirror(temp)
        outframes.append(temp)
    return outframes


async def ud_frames(image, w, h, outframes, flip=False):
    for i in range(1, h, h // 30):
        img1 = img2 = image.copy()
        temp = Image.new("RGB", (w, h))
        img1 = img1.resize((w, i))
        img2 = img2.resize((w, h - i))
        temp.paste(img1, (0, 0))
        temp.paste(img2, (0, i))
        if flip:
            temp = ImageOps.flip(temp)
        outframes.append(temp)
    return outframes


async def spin_frames(image, w, h, outframes):
    image.thumbnail((512, 512), Image.LANCZOS)
    img = Image.new("RGB", (512, 512), "black")
    img.paste(image, ((512 - w) // 2, (512 - h) // 2))
    image = img
    way = random.choice([1, -1])
    for i in range(1, 60):
        img = image.rotate(i * 6 * way)
        outframes.append(img)
    return outframes


async def invert_frames(image, w, h, outframes):
    image.convert("RGB")
    invert = ImageOps.invert(image)
    outframes.append(image)
    outframes.append(invert)
    return outframes


# ───── خطوط emojify ─────
class emojify:
    pass
_ns = {}
exec(compile('normaltext = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\nsmallcapsfont = "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ1234567890\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\nsuperscriptfont = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᵠᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ¹²³⁴⁵⁶⁷⁸⁹⁰\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\nsubscriptfont = "ₐBCDₑFGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥWₓYZₐᵦ𝒸𝒹ₑ𝒻𝓰ₕᵢⱼₖₗₘₙₒₚᵩᵣₛₜᵤᵥ𝓌ₓᵧ𝓏₁₂₃₄₅₆₇₈₉₀\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\nbubblesfont = "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ1234567890\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\nbubblesblackfont = "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩1234567890\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\nsmothtextfont = "ᗩᗷᑕᗞᗴᖴᏀᕼᏆᒍᏦᏞᗰᑎᝪᑭᑫᖇᔑᎢᑌᐯᗯ᙭ᎩᏃᗩᗷᑕᗞᗴᖴᏀᕼᏆᒍᏦᏞᗰᑎᝪᑭᑫᖇᔑᎢᑌᐯᗯ᙭ᎩᏃ1234567890\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\negyptfontfont = "ค๒ς๔єŦﻮђเןкl๓ภ๏קợгรtยשฬץאzค๒ς๔єŦﻮђเןкl๓ภ๏קợгรtยשฬץאz1234567890\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\nhwslfont = "𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏1234567890\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\nnightmarefont = "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟1234567890\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\nghostfontfont = "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅1234567890\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\nhwcapitalfont = "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩1234567890\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\ntantextfont = "ᎯᏰᏣᎴᏋᎴᎶᏂiᏠᏦlmᏁᏫᎵᏄᖇᎦᎿᏌᏉᏯﾒᎩᏃᎯᏰᏣᎴᏋᎴᎶᏂiᏠᏦlmᏁᏫᎵᏄᖇᎦᎿᏌᏉᏯﾒᎩᏃ1234567890\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\nlittleboxtextfont = "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉1234567890\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\ndoubletextfont = "ᎯℬℂⅅℰℱᎶℋℐᎫᏦℒℳℕᎾℙℚℛЅᏆUᏉᏇXᎽℤᎯℬℂⅅℰℱᎶℋℐᎫᏦℒℳℕᎾℙℚℛЅᏆUᏉᏇXᎽℤ1234567890\\"\'#$%&()*+,-./:;<=>?@[\\\\]^_`{|}~"\n\nupsidefont = [\n    "a",\n    "b",\n    "c",\n    "d",\n    "e",\n    "f",\n    "g",\n    "h",\n    "i",\n    "j",\n    "k",\n    "l",\n    "m",\n    "n",\n    "o",\n    "p",\n    "q",\n    "r",\n    "s",\n    "t",\n    "u",\n    "v",\n    "w",\n    "x",\n    "y",\n    "z",\n    "A",\n    "B",\n    "C",\n    "D",\n    "E",\n    "F",\n    "G",\n    "H",\n    "I",\n    "J",\n    "K",\n    "L",\n    "M",\n    "N",\n    "O",\n    "P",\n    "Q",\n    "R",\n    "S",\n    "T",\n    "U",\n    "V",\n    "W",\n    "X",\n    "Y",\n    "Z",\n    "0",\n    "1",\n    "2",\n    "3",\n    "4",\n    "5",\n    "6",\n    "7",\n    "8",\n    "9",\n    "_",\n    "\'",\n    ",",\n    "\\\\",\n    "/",\n    "!",\n    "?",\n]\n\ndownsidefont = [\n    "ɐ",\n    "q",\n    "ɔ",\n    "p",\n    "ə",\n    "ɟ",\n    "ɓ",\n    "ɥ",\n    "ı",\n    "ɾ",\n    "ʞ",\n    "l",\n    "ɯ",\n    "u",\n    "o",\n    "p",\n    "q",\n    "ɹ",\n    "s",\n    "ʇ",\n    "n",\n    "ʌ",\n    "ʍ",\n    "x",\n    "ʎ",\n    "z",\n    "∀",\n    "B",\n    "Ↄ",\n    "◖",\n    "Ǝ",\n    "Ⅎ",\n    "⅁",\n    "H",\n    "I",\n    "ſ",\n    "K",\n    "⅂",\n    "W",\n    "ᴎ",\n    "O",\n    "Ԁ",\n    "Ό",\n    "ᴚ",\n    "S",\n    "⊥",\n    "∩",\n    "ᴧ",\n    "M",\n    "X",\n    "⅄",\n    "Z",\n    "0",\n    "1",\n    "ᄅ",\n    "Ɛ",\n    "ᔭ",\n    "5",\n    "9",\n    "Ɫ",\n    "8",\n    "6",\n    "¯",\n    ",",\n    "\'",\n    "/",\n    "\\\\",\n    "¡",\n    "¿",\n]\n\nancientfont = [\n    "ꍏ",\n    "ꌃ",\n    "ꉓ",\n    "ꀸ",\n    "ꍟ",\n    "ꎇ",\n    "ꁅ",\n    "ꃅ",\n    "ꀤ",\n    "ꀭ",\n    "ꀘ",\n    "꒒",\n    "ꎭ",\n    "ꈤ",\n    "ꂦ",\n    "ᖘ",\n    "ꆰ",\n    "ꋪ",\n    "ꌗ",\n    "꓄",\n    "ꀎ",\n    "ᐯ",\n    "ꅏ",\n    "ꊼ",\n    "ꌩ",\n    "ꁴ",\n    "ꍏ",\n    "ꌃ",\n    "ꉓ",\n    "ꀸ",\n    "ꍟ",\n    "ꎇ",\n    "ꁅ",\n    "ꃅ",\n    "ꀤ",\n    "ꀭ",\n    "ꀘ",\n    "꒒",\n    "ꎭ",\n    "ꈤ",\n    "ꂦ",\n    "ᖘ",\n    "ꆰ",\n    "ꋪ",\n    "ꌗ",\n    "꓄",\n    "ꀎ",\n    "ᐯ",\n    "ꅏ",\n    "ꊼ",\n    "ꌩ",\n    "ꁴ",\n    "0",\n    "1",\n    "2",\n    "3",\n    "4",\n    "5",\n    "6",\n    "7",\n    "8",\n    "9",\n    "_",\n    "\'",\n    ",",\n    "\\\\",\n    "/",\n    "!",\n    "?",\n]\n\nnormalfont = [\n    "a",\n    "b",\n    "c",\n    "d",\n    "e",\n    "f",\n    "g",\n    "h",\n    "i",\n    "j",\n    "k",\n    "l",\n    "m",\n    "n",\n    "o",\n    "p",\n    "q",\n    "r",\n    "s",\n    "t",\n    "u",\n    "v",\n    "w",\n    "x",\n    "y",\n    "z",\n    "A",\n    "B",\n    "C",\n    "D",\n    "E",\n    "F",\n    "G",\n    "H",\n    "I",\n    "J",\n    "K",\n    "L",\n    "M",\n    "N",\n    "O",\n    "P",\n    "Q",\n    "R",\n    "S",\n    "T",\n    "U",\n    "V",\n    "W",\n    "X",\n    "Y",\n    "Z",\n    "0",\n    "1",\n    "2",\n    "3",\n    "4",\n    "5",\n    "6",\n    "7",\n    "8",\n    "9",\n    "_",\n    "\'",\n    ",",\n    "\\\\",\n    "/",\n    "!",\n    "?",\n]\n\nmusicalfont = [\n    "♬",\n    "ᖲ",\n    "¢",\n    "ᖱ",\n    "៩",\n    "⨏",\n    "❡",\n    "Ϧ",\n    "ɨ",\n    "ɉ",\n    "ƙ",\n    "ɭ",\n    "៣",\n    "⩎",\n    "០",\n    "ᖰ",\n    "ᖳ",\n    "Ʀ",\n    "ន",\n    "Ƭ",\n    "⩏",\n    "⩔",\n    "Ɯ",\n    "✗",\n    "ƴ",\n    "Ȥ",\n    "♬",\n    "ᖲ",\n    "¢",\n    "ᖱ",\n    "៩",\n    "⨏",\n    "❡",\n    "Ϧ",\n    "ɨ",\n    "ɉ",\n    "ƙ",\n    "ɭ",\n    "៣",\n    "⩎",\n    "០",\n    "ᖰ",\n    "ᖳ",\n    "Ʀ",\n    "ន",\n    "Ƭ",\n    "⩏",\n    "⩔",\n    "Ɯ",\n    "✗",\n    "ƴ",\n    "Ȥ",\n    "0",\n    "1",\n    "2",\n    "3",\n    "4",\n    "5",\n    "6",\n    "7",\n    "8",\n    "9",\n    "_",\n    "\'",\n    ",",\n    "\\\\",\n    "/",\n    "!",\n    "?",\n]\n\n\nnormiefont = [\n    "a",\n    "b",\n    "c",\n    "d",\n    "e",\n    "f",\n    "g",\n    "h",\n    "i",\n    "j",\n    "k",\n    "l",\n    "m",\n    "n",\n    "o",\n    "p",\n    "q",\n    "r",\n    "s",\n    "t",\n    "u",\n    "v",\n    "w",\n    "x",\n    "y",\n    "z",\n]\n\nweebyfont = [\n    "卂",\n    "乃",\n    "匚",\n    "刀",\n    "乇",\n    "下",\n    "厶",\n    "卄",\n    "工",\n    "丁",\n    "长",\n    "乚",\n    "从",\n    "𠘨",\n    "口",\n    "尸",\n    "㔿",\n    "尺",\n    "丂",\n    "丅",\n    "凵",\n    "リ",\n    "山",\n    "乂",\n    "丫",\n    "乙",\n]\n\nEMOJIS = [\n    "😂",\n    "😂",\n    "👌",\n    "💞",\n    "👍",\n    "👌",\n    "💯",\n    "🎶",\n    "👀",\n    "😂",\n    "👓",\n    "👏",\n    "👐",\n    "🍕",\n    "💥",\n    "😩",\n    "😏",\n    "😞",\n    "👀",\n    "👅",\n    "😩",\n    "🤒",\n    "😳",\n    "🤯",\n    "😵",\n    "🥵",\n    "🤒",\n    "😠",\n    "😪",\n    "😴",\n    "🤤",\n    "👿",\n    "👽",\n    "😏",\n    "😒",\n    "😣",\n    "🤔",\n    "🤨",\n    "🧐",\n    "😝",\n    "🤪",\n    "🤩",\n    "☺️",\n    "😭",\n    "🥺",\n]\n\nZALG_LIST = [\n    [\n        "̖",\n        " ̗",\n        " ̘",\n        " ̙",\n        " ̜",\n        " ̝",\n        " ̞",\n        " ̟",\n        " ̠",\n        " ̤",\n        " ̥",\n        " ̦",\n        " ̩",\n        " ̪",\n        " ̫",\n        " ̬",\n        " ̭",\n        " ̮",\n        " ̯",\n        " ̰",\n        " ̱",\n        " ̲",\n        " ̳",\n        " ̹",\n        " ̺",\n        " ̻",\n        " ̼",\n        " ͅ",\n        " ͇",\n        " ͈",\n        " ͉",\n        " ͍",\n        " ͎",\n        " ͓",\n        " ͔",\n        " ͕",\n        " ͖",\n        " ͙",\n        " ͚",\n        " ",\n    ],\n    [\n        " ̍",\n        " ̎",\n        " ̄",\n        " ̅",\n        " ̿",\n        " ̑",\n        " ̆",\n        " ̐",\n        " ͒",\n        " ͗",\n        " ͑",\n        " ̇",\n        " ̈",\n        " ̊",\n        " ͂",\n        " ̓",\n        " ̈́",\n        " ͊",\n        " ͋",\n        " ͌",\n        " ̃",\n        " ̂",\n        " ̌",\n        " ͐",\n        " ́",\n        " ̋",\n        " ̏",\n        " ̽",\n        " ̉",\n        " ͣ",\n        " ͤ",\n        " ͥ",\n        " ͦ",\n        " ͧ",\n        " ͨ",\n        " ͩ",\n        " ͪ",\n        " ͫ",\n        " ͬ",\n        " ͭ",\n        " ͮ",\n        " ͯ",\n        " ̾",\n        " ͛",\n        " ͆",\n        " ̚",\n    ],\n    [\n        " ̕",\n        " ̛",\n        " ̀",\n        " ́",\n        " ͘",\n        " ̡",\n        " ̢",\n        " ̧",\n        " ̨",\n        " ̴",\n        " ̵",\n        " ̶",\n        " ͜",\n        " ͝",\n        " ͞",\n        " ͟",\n        " ͠",\n        " ͢",\n        " ̸",\n        " ̷",\n        " ͡",\n    ],\n]\n\nkakashitext = [\n    "a",\n    "b",\n    "c",\n    "d",\n    "e",\n    "f",\n    "g",\n    "h",\n    "i",\n    "j",\n    "k",\n    "l",\n    "m",\n    "n",\n    "o",\n    "p",\n    "q",\n    "r",\n    "s",\n    "t",\n    "u",\n    "v",\n    "w",\n    "x",\n    "y",\n    "z",\n    "0",\n    "1",\n    "2",\n    "3",\n    "4",\n    "5",\n    "6",\n    "7",\n    "8",\n    "9",\n]\n\n\nkakashiemoji = [\n    "\u206d\\n                    💖\\n                  💖💖\\n               💖💖💖\\n            💖💖 💖💖\\n          💖💖    💖💖\\n        💖💖       💖💖\\n      💖💖💖💖💖💖\\n     💖💖💖💖💖💖💖\\n   💖💖                 💖💖\\n  💖💖                    💖💖\\n💖💖                       💖💖\\n",\n    "\u206d\\n💗💗💗💗💗💗💗\\n💗💗💗💗💗💗💗💗\\n💗💗                     💗💗\\n💗💗                     💗💗\\n💗💗💗💗💗💗💗💗\\n💗💗💗💗💗💗💗💗\\n💗💗                     💗💗\\n💗💗                     💗💗\\n💗💗💗💗💗💗💗💗\\n💗💗💗💗💗💗💗\\n",\n    "\u206d\\n          💛💛💛💛💛💛\\n     💛💛💛💛💛💛💛💛\\n   💛💛                      💛💛\\n 💛💛\\n💛💛\\n💛💛\\n 💛💛\\n   💛💛                      💛💛\\n     💛💛💛💛💛💛💛💛\\n         💛💛💛💛💛💛\\n",\n    "\u206d\\n💙💙💙💙💙💙💙\\n💙💙💙💙💙💙💙💙\\n💙💙                      💙💙\\n💙💙                         💙💙\\n💙💙                         💙💙\\n💙💙                         💙💙\\n💙💙                         💙💙\\n💙💙                      💙💙\\n💙💙💙💙💙💙💙💙\\n💙💙💙💙💙💙💙\\n",\n    "\u206d\\n💟💟💟💟💟💟💟💟\\n💟💟💟💟💟💟💟💟\\n💟💟\\n💟💟\\n💟💟💟💟💟💟\\n💟💟💟💟💟💟\\n💟💟\\n💟💟\\n💟💟💟💟💟💟💟💟\\n💟💟💟💟💟💟💟💟\\n",\n    "\u206d\\n💚💚💚💚💚💚💚💚\\n💚💚💚💚💚💚💚💚\\n💚💚\\n💚💚\\n💚💚💚💚💚💚\\n💚💚💚💚💚💚\\n💚💚\\n💚💚\\n💚💚\\n💚💚\\n",\n    "\u206d\\n          💜💜💜💜💜💜\\n     💜💜💜💜💜💜💜💜\\n   💜💜                     💜💜\\n 💜💜\\n💜💜                💜💜💜💜\\n💜💜                💜💜💜💜\\n 💜💜                        💜💜\\n   💜💜                      💜💜\\n     💜💜💜💜💜💜💜💜\\n          💜💜💜💜💜💜\\n",\n    "\u206d\\n💖💖                        💖💖\\n💖💖                        💖💖\\n💖💖                        💖💖\\n💖💖                        💖💖\\n💖💖💖💖💖💖💖💖💖\\n💖💖💖💖💖💖💖💖💖\\n💖💖                        💖💖\\n💖💖                        💖💖\\n💖💖                        💖💖\\n💖💖                        💖💖\\n",\n    "\u206d\\n💗💗💗💗💗💗\\n💗💗💗💗💗💗\\n          💗💗\\n          💗💗\\n          💗💗\\n          💗💗\\n          💗💗\\n          💗💗\\n💗💗💗💗💗💗\\n💗💗💗💗💗💗\\n",\n    "\u206d\\n         💛💛💛💛💛💛\\n         💛💛💛💛💛💛\\n                  💛💛\\n                  💛💛\\n                  💛💛\\n                  💛💛\\n💛💛          💛💛\\n  💛💛       💛💛\\n   💛💛💛💛💛\\n      💛💛💛💛\\n",\n    "\u206d\\n💙💙                  💙💙\\n💙💙             💙💙\\n💙💙        💙💙\\n💙💙   💙💙\\n💙💙💙💙\\n💙💙 💙💙\\n💙💙     💙💙\\n💙💙         💙💙\\n💙💙              💙💙\\n💙💙                   💙💙\\n",\n    "\u206d\\n💟💟\\n💟💟\\n💟💟\\n💟💟\\n💟💟\\n💟💟\\n💟💟\\n💟💟\\n💟💟💟💟💟💟💟💟\\n💟💟💟💟💟💟💟💟\\n",\n    "\u206d\\n💚💚                              💚💚\\n💚💚💚                      💚💚💚\\n💚💚💚💚            💚💚💚💚\\n💚💚    💚💚    💚💚    💚💚\\n💚💚        💚💚💚        💚💚\\n💚💚             💚             💚💚\\n💚💚                              💚💚\\n💚💚                              💚💚\\n💚💚                              💚💚\\n💚💚                              💚💚\\n",\n    "\u206d\\n💜💜                           💜💜\\n💜💜💜                       💜💜\\n💜💜💜💜                 💜💜\\n💜💜  💜💜               💜💜\\n💜💜     💜💜            💜💜\\n💜💜         💜💜        💜💜\\n💜💜             💜💜    💜💜\\n💜💜                 💜💜💜💜\\n💜💜                     💜💜💜\\n💜💜                          💜💜\\n",\n    "\u206d\\n           💖💖💖💖💖\\n     💖💖💖💖💖💖💖\\n   💖💖                   💖💖\\n 💖💖                       💖💖\\n💖💖                         💖💖\\n💖💖                         💖💖\\n 💖💖                       💖💖\\n   💖💖                   💖💖\\n      💖💖💖💖💖💖💖\\n            💖💖💖💖💖\\n",\n    "\u206d\\n💗💗💗💗💗💗💗\\n💗💗💗💗💗💗💗💗\\n💗💗                     💗💗\\n💗💗                     💗💗\\n💗💗💗💗💗💗💗💗\\n💗💗💗💗💗💗💗\\n💗💗\\n💗💗\\n💗💗\\n💗💗\\n",\n    "\u206d\\n           💛💛💛💛💛\\n      💛💛💛💛💛💛💛\\n   💛💛                    💛💛\\n 💛💛                        💛💛\\n💛💛                           💛💛\\n💛💛              💛💛     💛💛\\n 💛💛               💛💛 💛💛\\n   💛💛                   💛💛\\n      💛💛💛💛💛💛💛💛\\n           💛💛💛💛💛   💛💛\\n",\n    "\u206d\\n💙💙💙💙💙💙💙\\n💙💙💙💙💙💙💙💙\\n💙💙                     💙💙\\n💙💙                     💙💙\\n💙💙💙💙💙💙💙💙\\n💙💙💙💙💙💙💙\\n💙💙    💙💙\\n💙💙         💙💙\\n💙💙              💙💙\\n💙💙                  💙💙\\n",\n    "\u206d\\n       💟💟💟💟💟\\n  💟💟💟💟💟💟💟\\n  💟💟                 💟💟\\n💟💟\\n  💟💟💟💟💟💟\\n      💟💟💟💟💟💟\\n                            💟💟\\n💟💟                 💟💟\\n  💟💟💟💟💟💟💟\\n       💟💟💟💟💟\\n",\n    "\u206d\\n💚💚💚💚💚💚💚💚\\n💚💚💚💚💚💚💚💚\\n               💚💚\\n               💚💚\\n               💚💚\\n               💚💚\\n               💚💚\\n               💚💚\\n               💚💚\\n",\n    "\u206d\\n💜💜                      💜💜\\n💜💜                      💜💜\\n💜💜                      💜💜\\n💜💜                      💜💜\\n💜💜                      💜💜\\n💜💜                      💜💜\\n💜💜                      💜💜\\n  💜💜                  💜💜\\n      💜💜💜💜💜💜\\n            💜💜💜💜\\n",\n    "\u206d\\n💖💖                              💖💖\\n  💖💖                          💖💖\\n    💖💖                      💖💖\\n      💖💖                  💖💖\\n         💖💖              💖💖\\n           💖💖         💖💖\\n             💖💖     💖💖\\n               💖💖 💖💖\\n                  💖💖💖\\n                       💖\\n",\n    "\u206d\\n💗💗                               💗💗\\n💗💗                               💗💗\\n💗💗                               💗💗\\n💗💗                               💗💗\\n💗💗              💗            💗💗\\n 💗💗           💗💗          💗💗\\n 💗💗        💗💗💗       💗💗\\n  💗💗   💗💗  💗💗   💗💗\\n   💗💗💗💗      💗💗💗💗\\n    💗💗💗             💗💗💗\\n",\n    "\u206d\\n💛💛                    💛💛\\n   💛💛              💛💛\\n      💛💛        💛💛\\n         💛💛  💛💛\\n            💛💛💛\\n            💛💛💛\\n         💛💛 💛💛\\n      💛💛       💛💛\\n   💛💛             💛💛\\n💛💛                   💛💛\\n",\n    "\u206d\\n💙💙                    💙💙\\n   💙💙              💙💙\\n      💙💙        💙💙\\n         💙💙  💙💙\\n            💙💙💙\\n              💙💙\\n              💙💙\\n              💙💙\\n              💙💙\\n              💙💙\\n",\n    "\u206d\\n 💟💟💟💟💟💟💟\\n 💟💟💟💟💟💟💟\\n                       💟💟\\n                   💟💟\\n               💟💟\\n           💟💟\\n       💟💟\\n   💟💟\\n💟💟💟💟💟💟💟\\n💟💟💟💟💟💟💟\\n",\n    "\u206d\\n       💗💗💗💗\\n   💗💗💗💗💗💗\\n💗💗               💗💗\\n💗💗               💗💗\\n💗💗               💗💗\\n💗💗               💗💗\\n💗💗               💗💗\\n💗💗               💗💗\\n   💗💗💗💗💗💗\\n        💗💗💗💗\\n",\n    "\u206d\\n          💙💙\\n     💙💙💙\\n💙💙 💙💙\\n          💙💙\\n          💙💙\\n          💙💙\\n          💙💙\\n          💙💙\\n     💙💙💙💙\\n     💙💙💙💙\\n",\n    "\u206d\\n    💟💟💟💟💟\\n  💟💟💟💟💟💟\\n💟💟          💟💟\\n                💟💟\\n             💟💟\\n          💟💟\\n       💟💟\\n    💟💟\\n  💟💟💟💟💟💟\\n  💟💟💟💟💟💟\\n",\n    "\u206d\\n     💛💛💛💛\\n  💛💛💛💛💛\\n💛💛         💛💛\\n                   💛💛\\n            💛💛💛\\n            💛💛💛\\n                   💛💛\\n💛💛         💛💛\\n  💛💛💛💛💛\\n     💛💛💛💛\\n",\n    "\u206d\\n                         💖💖\\n                    💖💖💖\\n              💖💖 💖💖\\n          💖💖     💖💖\\n     💖💖          💖💖\\n💖💖               💖💖\\n💖💖💖💖💖💖💖💖💖\\n💖💖💖💖💖💖💖💖💖\\n                         💖💖\\n                         💖💖\\n",\n    "\u206d\\n💚💚💚💚💚💚\\n💚💚💚💚💚💚\\n💚💚\\n 💚💚💚💚💚\\n   💚💚💚💚💚\\n                    💚💚\\n                    💚💚\\n💚💚          💚💚\\n  💚💚💚💚💚\\n     💚💚💚💚\\n",\n    "\u206d\\n        💜💜💜💜\\n    💜💜💜💜💜\\n💜💜\\n\\n💜💜\\n💜💜💜💜💜💜\\n💜💜💜💜💜💜💜\\n💜💜               💜💜\\n💜💜               💜💜\\n    💜💜💜💜💜💜\\n        💜💜💜💜\\n",\n    "\u206d\\n💗💗💗💗💗💗💗\\n💗💗💗💗💗💗💗\\n                      💗💗\\n                     💗💗\\n                   💗💗\\n                 💗💗\\n               💗💗\\n             💗💗\\n           💗💗\\n         💗💗\\n",\n    "\u206d\\n        💙💙💙💙\\n   💙💙💙💙💙💙\\n💙💙               💙💙\\n💙💙               💙💙\\n   💙💙💙💙💙💙\\n   💙💙💙💙💙💙\\n💙💙               💙💙\\n💙💙               💙💙\\n   💙💙💙💙💙💙\\n        💙💙💙💙\\n",\n    "\u206d\\n        💟💟💟💟\\n   💟💟💟💟💟💟\\n💟💟               💟💟\\n💟💟               💟💟\\n 💟💟💟💟💟💟💟\\n      💟💟💟💟💟💟\\n                         💟💟\\n                        💟💟\\n  💟💟💟💟💟💟\\n       💟💟💟💟\\n",\n]\n\n\nitachiemoji = [\n    "\u206d\\n                    {cj}\\n                  {cj}{cj}\\n               {cj}{cj}{cj}\\n            {cj}{cj} {cj}{cj}\\n          {cj}{cj}    {cj}{cj}\\n        {cj}{cj}       {cj}{cj}\\n      {cj}{cj}{cj}{cj}{cj}{cj}\\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n   {cj}{cj}                 {cj}{cj}\\n  {cj}{cj}                    {cj}{cj}\\n{cj}{cj}                       {cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}                     {cj}{cj}\\n{cj}{cj}                     {cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}                     {cj}{cj}\\n{cj}{cj}                     {cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n          {cj}{cj}{cj}{cj}{cj}{cj}\\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n   {cj}{cj}                      {cj}{cj}\\n {cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n {cj}{cj}\\n   {cj}{cj}                      {cj}{cj}\\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n         {cj}{cj}{cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}                      {cj}{cj}\\n{cj}{cj}                         {cj}{cj}\\n{cj}{cj}                         {cj}{cj}\\n{cj}{cj}                         {cj}{cj}\\n{cj}{cj}                         {cj}{cj}\\n{cj}{cj}                      {cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n",\n    "\u206d\\n          {cj}{cj}{cj}{cj}{cj}{cj}\\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n   {cj}{cj}                     {cj}{cj}\\n {cj}{cj}\\n{cj}{cj}                {cj}{cj}{cj}{cj}\\n{cj}{cj}                {cj}{cj}{cj}{cj}\\n {cj}{cj}                        {cj}{cj}\\n   {cj}{cj}                      {cj}{cj}\\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n          {cj}{cj}{cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}                        {cj}{cj}\\n{cj}{cj}                        {cj}{cj}\\n{cj}{cj}                        {cj}{cj}\\n{cj}{cj}                        {cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}                        {cj}{cj}\\n{cj}{cj}                        {cj}{cj}\\n{cj}{cj}                        {cj}{cj}\\n{cj}{cj}                        {cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}\\n          {cj}{cj}\\n          {cj}{cj}\\n          {cj}{cj}\\n          {cj}{cj}\\n          {cj}{cj}\\n          {cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n         {cj}{cj}{cj}{cj}{cj}{cj}\\n         {cj}{cj}{cj}{cj}{cj}{cj}\\n                  {cj}{cj}\\n                  {cj}{cj}\\n                  {cj}{cj}\\n                  {cj}{cj}\\n{cj}{cj}          {cj}{cj}\\n  {cj}{cj}       {cj}{cj}\\n   {cj}{cj}{cj}{cj}{cj}\\n      {cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}                  {cj}{cj}\\n{cj}{cj}             {cj}{cj}\\n{cj}{cj}        {cj}{cj}\\n{cj}{cj}   {cj}{cj}\\n{cj}{cj}{cj}{cj}\\n{cj}{cj} {cj}{cj}\\n{cj}{cj}     {cj}{cj}\\n{cj}{cj}         {cj}{cj}\\n{cj}{cj}              {cj}{cj}\\n{cj}{cj}                   {cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}                              {cj}{cj}\\n{cj}{cj}{cj}                      {cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}            {cj}{cj}{cj}{cj}\\n{cj}{cj}    {cj}{cj}    {cj}{cj}    {cj}{cj}\\n{cj}{cj}        {cj}{cj}{cj}        {cj}{cj}\\n{cj}{cj}             {cj}             {cj}{cj}\\n{cj}{cj}                              {cj}{cj}\\n{cj}{cj}                              {cj}{cj}\\n{cj}{cj}                              {cj}{cj}\\n{cj}{cj}                              {cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}                           {cj}{cj}\\n{cj}{cj}{cj}                       {cj}{cj}\\n{cj}{cj}{cj}{cj}                 {cj}{cj}\\n{cj}{cj}  {cj}{cj}               {cj}{cj}\\n{cj}{cj}     {cj}{cj}            {cj}{cj}\\n{cj}{cj}         {cj}{cj}        {cj}{cj}\\n{cj}{cj}             {cj}{cj}    {cj}{cj}\\n{cj}{cj}                 {cj}{cj}{cj}{cj}\\n{cj}{cj}                     {cj}{cj}{cj}\\n{cj}{cj}                          {cj}{cj}\\n",\n    "\u206d\\n           {cj}{cj}{cj}{cj}{cj}\\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n   {cj}{cj}                   {cj}{cj}\\n {cj}{cj}                       {cj}{cj}\\n{cj}{cj}                         {cj}{cj}\\n{cj}{cj}                         {cj}{cj}\\n {cj}{cj}                       {cj}{cj}\\n   {cj}{cj}                   {cj}{cj}\\n      {cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n            {cj}{cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}                     {cj}{cj}\\n{cj}{cj}                     {cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n{cj}{cj}\\n",\n    "\u206d\\n           {cj}{cj}{cj}{cj}{cj}\\n      {cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n   {cj}{cj}                    {cj}{cj}\\n {cj}{cj}                        {cj}{cj}\\n{cj}{cj}                           {cj}{cj}\\n{cj}{cj}              {cj}{cj}     {cj}{cj}\\n {cj}{cj}               {cj}{cj} {cj}{cj}\\n   {cj}{cj}                   {cj}{cj}\\n      {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n           {cj}{cj}{cj}{cj}{cj}   {cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}                     {cj}{cj}\\n{cj}{cj}                     {cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}    {cj}{cj}\\n{cj}{cj}         {cj}{cj}\\n{cj}{cj}              {cj}{cj}\\n{cj}{cj}                  {cj}{cj}\\n",\n    "\u206d\\n       {cj}{cj}{cj}{cj}{cj}\\n  {cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n  {cj}{cj}                 {cj}{cj}\\n{cj}{cj}\\n  {cj}{cj}{cj}{cj}{cj}{cj}\\n      {cj}{cj}{cj}{cj}{cj}{cj}\\n                            {cj}{cj}\\n{cj}{cj}                 {cj}{cj}\\n  {cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n       {cj}{cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n               {cj}{cj}\\n               {cj}{cj}\\n               {cj}{cj}\\n               {cj}{cj}\\n               {cj}{cj}\\n               {cj}{cj}\\n               {cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}                      {cj}{cj}\\n{cj}{cj}                      {cj}{cj}\\n{cj}{cj}                      {cj}{cj}\\n{cj}{cj}                      {cj}{cj}\\n{cj}{cj}                      {cj}{cj}\\n{cj}{cj}                      {cj}{cj}\\n{cj}{cj}                      {cj}{cj}\\n  {cj}{cj}                  {cj}{cj}\\n      {cj}{cj}{cj}{cj}{cj}{cj}\\n            {cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}                              {cj}{cj}\\n  {cj}{cj}                          {cj}{cj}\\n    {cj}{cj}                      {cj}{cj}\\n      {cj}{cj}                  {cj}{cj}\\n         {cj}{cj}              {cj}{cj}\\n           {cj}{cj}         {cj}{cj}\\n             {cj}{cj}     {cj}{cj}\\n               {cj}{cj} {cj}{cj}\\n                  {cj}{cj}{cj}\\n                       {cj}\\n",\n    "\u206d\\n{cj}{cj}                               {cj}{cj}\\n{cj}{cj}                               {cj}{cj}\\n{cj}{cj}                               {cj}{cj}\\n{cj}{cj}                               {cj}{cj}\\n{cj}{cj}              {cj}            {cj}{cj}\\n {cj}{cj}           {cj}{cj}          {cj}{cj}\\n {cj}{cj}        {cj}{cj}{cj}       {cj}{cj}\\n  {cj}{cj}   {cj}{cj}  {cj}{cj}   {cj}{cj}\\n   {cj}{cj}{cj}{cj}      {cj}{cj}{cj}{cj}\\n    {cj}{cj}{cj}             {cj}{cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}                    {cj}{cj}\\n   {cj}{cj}              {cj}{cj}\\n      {cj}{cj}        {cj}{cj}\\n         {cj}{cj}  {cj}{cj}\\n            {cj}{cj}{cj}\\n            {cj}{cj}{cj}\\n         {cj}{cj} {cj}{cj}\\n      {cj}{cj}       {cj}{cj}\\n   {cj}{cj}             {cj}{cj}\\n{cj}{cj}                   {cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}                    {cj}{cj}\\n   {cj}{cj}              {cj}{cj}\\n      {cj}{cj}        {cj}{cj}\\n         {cj}{cj}  {cj}{cj}\\n            {cj}{cj}{cj}\\n              {cj}{cj}\\n              {cj}{cj}\\n              {cj}{cj}\\n              {cj}{cj}\\n              {cj}{cj}\\n",\n    "\u206d\\n {cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n {cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n                       {cj}{cj}\\n                   {cj}{cj}\\n               {cj}{cj}\\n           {cj}{cj}\\n       {cj}{cj}\\n   {cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n       {cj}{cj}{cj}{cj}\\n   {cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n   {cj}{cj}{cj}{cj}{cj}{cj}\\n        {cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n          {cj}{cj}\\n     {cj}{cj}{cj}\\n{cj}{cj} {cj}{cj}\\n          {cj}{cj}\\n          {cj}{cj}\\n          {cj}{cj}\\n          {cj}{cj}\\n          {cj}{cj}\\n     {cj}{cj}{cj}{cj}\\n     {cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n    {cj}{cj}{cj}{cj}{cj}\\n  {cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}          {cj}{cj}\\n                {cj}{cj}\\n             {cj}{cj}\\n          {cj}{cj}\\n       {cj}{cj}\\n    {cj}{cj}\\n  {cj}{cj}{cj}{cj}{cj}{cj}\\n  {cj}{cj}{cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n     {cj}{cj}{cj}{cj}\\n  {cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}         {cj}{cj}\\n                   {cj}{cj}\\n            {cj}{cj}{cj}\\n            {cj}{cj}{cj}\\n                   {cj}{cj}\\n{cj}{cj}         {cj}{cj}\\n  {cj}{cj}{cj}{cj}{cj}\\n     {cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n                         {cj}{cj}\\n                    {cj}{cj}{cj}\\n              {cj}{cj} {cj}{cj}\\n          {cj}{cj}     {cj}{cj}\\n     {cj}{cj}          {cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n                         {cj}{cj}\\n                         {cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}\\n {cj}{cj}{cj}{cj}{cj}\\n   {cj}{cj}{cj}{cj}{cj}\\n                    {cj}{cj}\\n                    {cj}{cj}\\n{cj}{cj}          {cj}{cj}\\n  {cj}{cj}{cj}{cj}{cj}\\n     {cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n        {cj}{cj}{cj}{cj}\\n    {cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}\\n\\n{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n    {cj}{cj}{cj}{cj}{cj}{cj}\\n        {cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n                      {cj}{cj}\\n                     {cj}{cj}\\n                   {cj}{cj}\\n                 {cj}{cj}\\n               {cj}{cj}\\n             {cj}{cj}\\n           {cj}{cj}\\n         {cj}{cj}\\n",\n    "\u206d\\n        {cj}{cj}{cj}{cj}\\n   {cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n   {cj}{cj}{cj}{cj}{cj}{cj}\\n   {cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n   {cj}{cj}{cj}{cj}{cj}{cj}\\n        {cj}{cj}{cj}{cj}\\n",\n    "\u206d\\n        {cj}{cj}{cj}{cj}\\n   {cj}{cj}{cj}{cj}{cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n{cj}{cj}               {cj}{cj}\\n {cj}{cj}{cj}{cj}{cj}{cj}{cj}\\n      {cj}{cj}{cj}{cj}{cj}{cj}\\n                         {cj}{cj}\\n                        {cj}{cj}\\n  {cj}{cj}{cj}{cj}{cj}{cj}\\n       {cj}{cj}{cj}{cj}\\n",\n]', "fonts", "exec"), _ns)
for _k, _v in _ns.items():
    if not _k.startswith("__"):
        setattr(emojify, _k, _v)
