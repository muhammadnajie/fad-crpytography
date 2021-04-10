from PIL import Image
import re


def dec_to_bin(decimal):
    return re.sub("0b", "", bin(decimal))


def load_and_convert_msg(txt):
    """Load message text from a file and convert it into binary code"""
    bin_code = []
    with open(txt) as msg:
        for line in msg:
            for c in line:
                bin_code.append(dec_to_bin(ord(c)))
    return bin_code

def to_even(color):
    """Convert every primary color hexanumber to even"""
    for idx, value in enumerate(color):
        value = value >> 1
        value = value << 1
        color[idx] = value
    return color


def lsb_normalization(pix, size):
    for row in range(size[0]):
        for col in range(size[1]):
            rgb = to_even(list(pix[row, col]))
            pix[row, col] = tuple(rgb)
    return pix

def lsb_rule(numb, bit):
    if numb % 2 == 0:
        return numb | bit

    if bit == 0:
        return numb-1
    return numb
    

def lsb(im, bin_msg):
    im_pix = im.load()
    im_pix = lsb_normalization(im_pix, im.size)
    bin_msg = "".join(bin_msg)
    # print(bin_msg)
    row = 0
    col = 0
    for i in range(0, len(bin_msg), 3):
        r_bit = int(bin_msg[i])
        try:
            g_bit = int(bin_msg[i+1])
        except:
            g_bit = 0
        
        try:
            b_bit = int(bin_msg[i+2])
        except:
            b_bit = 0
        r, g, b = im_pix[row, col]
        r, g, b = lsb_rule(r, r_bit), lsb_rule(g, g_bit), lsb_rule(b, b_bit)
        im_pix[row, col] = (r, g, b)

        col += 1

        if col + 1 > im.size[1]:
            row += 1
            col = 0


def main():
    bin_msg = load_and_convert_msg("msg.txt")
    im = Image.open('./hurt meow meow.jpg')
    pix = im.load()
    print([pix[0,i] for i in range(50)])
    lsb(im, bin_msg)
    print([pix[0,i] for i in range(50)])
    try:
        filename = "uwuw.jpg"
        im.save(filename)
        print("Berhasil menyisipkan pesan ke dalam gambar {}".format(filename))
    except:
        print("Penyisipan pesan gagal!")

# main()