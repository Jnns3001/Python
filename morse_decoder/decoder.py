def decode(message, debug=0):
    encodedChars = ["_*-_", "_-***_", "_-*-*_", "_-**_", "_*_", "_**-*_", "_--*_", "_****_", "_**_", "_*---_","_-*-_","_*-**_","_--_","_-*_","_---_","_*--*_","_--*-_","_*-*_","_***_","_-_","_**-_","_***-_","_*--_","_-**-_","_-*--_","_--**_","_*-*-*-_","_-*-*--_", "_--**--_", "_#_"]
    decodedChars = ["_a_", "_b_", "_c_", "_d_", "_e_", "_f_", "_g_", "_h_", "_i_", "_j_", "_k_", "_l_", "_m_", "_n_", "_o_", "_p_", "_q_", "_r_", "_s_", "_t_", "_u_", "_v_", "_w_", "_x_", "_y_", "_z_", "_._", "_!_", "_,_", "_ _"]

    m = message

    for char in m:
        for charEncode in encodedChars:
            if m.find(charEncode) >= 0:
                index = m.find(charEncode)
                length = len(charEncode)
                indexReplacement = encodedChars.index(charEncode)
                m = replace(m, index, length, decodedChars[indexReplacement])
                if debug == 1:                                                          #Enable Debugging Option
                    print("Index: " + str(index) + ", Decoded \"" + encodedChars[indexReplacement] + "\" to \"" + decodedChars[indexReplacement] + "\"")
                    print(m + "\n")
    
    m = m.replace("_", "")
    return m


def replace(message, index, length, replacement):
    firstPart = message[:index]
    secondPart = message[(index + length):]

    return(firstPart + replacement + secondPart)


if __name__ == "__main__":
    encodedFile = open("PYTHON\morse_decoder\morse.txt", "r")
    encodedText = encodedFile.read()
    encodedFile.close()

    decodedText = decode(encodedText, 1)
    print(decodedText)


