from RsInstrument.RsInstrument import RsInstrument
from tkinter import *

Resource_string_1 = 'TCPIP::192.168.0.158::INSTR'
instr = RsInstrument(Resource_string_1,True,False)




# ====================== Interface basica para teste ======================
class INICIO:
    def __init__(self,master=None):
        self.Container1 = Frame(master)
        self.Container1["width"] = 5
        self.Container1.pack()




# ====================== Comandos Rohde ======================
class comandos_Rohde:
    def Preset_Basic(Modo,Unit,ModeAtt,Range,RefLevel):
        #definicoes dos comandos da funcao
            #Declaracao do "Modo" - funcao para o analizador
                # REC - Receiver
                # RTIM - Realtime mode
                # SAN - Spectrum Analayzer mode
            #Declaracao do "Unit" - Unidade a ser utilizada
                # DBM = dBm
                # V   = Volts
                # A   = Amperes
                # W   = Wats
                # DBPW= dBPower_Wats
            #declaracao do "ModeAtt" - Liga e desliga o modo automatico da Atenuacao
                # ON - Ligado
                # OFF - Desligado
            #declaracao do "Range" - Range do equipamento em dBm (quando setado em dBm como unidade)
                #100DB
                #50DB
                #10DB
                #5DB
                #1DB
            #declaracao do "RefLevel" - Reference Level (Nivel de referencia)
                # <Valor>dBm
        instr.write_str("INST:SEL "+Modo) #Inicializa modo Espectro
        instr.write_str("CALC:UNIT:POW "+Unit) #Unidades de medida
        instr.write_str("INP:ATT:AUTO "+ModeAtt) #Modo de atenuação 
        instr.write_str("DISP:WIND:TRAC:Y "+Range) #Range de operação a 100 dB
        instr.write_str("DISP:TRAC:Y:RLEV "+str(RefLevel)+"dBm") #Reference Level
        instr.query_opc(3000)
    def Presets_Inicial(ValFreq,Span,RBW,VBW,ModoTrace):
        #Definicoes dos comandos da funcao
            #Declaracao do "ValFreq" - Valor de frequencia central
                #<Valor de frequencia> MHz
            #declaracao do "Span" - Modo selecao de Span
                #<Valor do Span> MHz
            #Declaracao do "RBW" - Funcao de selecao RBW
                #<Valor do RBW> kHz
            #Declaracao do VBW - Funcao de selecao VBW
                #<Valor do VBW> kHz
            #Declaracao do "ModoTrace" - Trace - selecao de modo
                #MAXH = Max Hold
                #AVER = Average
                #BLAN = Blank
                #MINH = Min hold - Minim Hold
                #VIEW = Frozen trace
                #WRIT = Clear Write trace mode
        instr.write_str("FREQ:CENT "+str(ValFreq)+"MHz")
        instr.write_str("SENS:FREQ:SPAN "+str(Span)+"MHz")
        instr.write_str("BAND "+str(RBW)+"kHz")
        instr.write_str("BAND:VID "+str(VBW)+"kHz")
        instr.write_str("DISP:WIND:TRAC:MODE "+ModoTrace)
        instr.query_opc(3000)



comandos_Rohde.Preset_Basic("SAN","DBM","ON","100DB",30)
comandos_Rohde.Presets_Inicial(2402,3,30,30,"MAXH")