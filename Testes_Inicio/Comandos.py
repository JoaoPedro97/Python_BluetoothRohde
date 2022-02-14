from RsInstrument.RsInstrument import RsInstrument
from tkinter import *
from tkinter import messagebox
import time
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
    def Preset_Basic(Modo,Unit,ModeAtt,Range,RefLevel,SWPAuto):
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
            #Declaracao do "SWPAuto" - Switch para o modo automatico do SweepTime
                # ON  - Automatico Ativado
                # OFF - Automatico Desativado
        instr.write_str("INST:SEL "+Modo) #Inicializa modo Espectro
        instr.write_str("CALC:UNIT:POW "+Unit) #Unidades de medida
        instr.write_str("INP:ATT:AUTO "+ModeAtt) #Modo de atenuação 
        instr.write_str("DISP:WIND:TRAC:Y "+Range) #Range de operação a 100 dB
        instr.write_str("DISP:TRAC:Y:RLEV "+str(RefLevel)+"dBm") #Reference Level
        instr.write_str("ESP:RANG1:SWE:TIME:AUTO "+SWPAuto) #Sweep Time Auto Switch
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


class Ensaios_temp:
    def Separacao_de_Canais_de_Salto():
        comandos_Rohde.Preset_Basic("SAN","DBM","ON","100DB",30,"ON")
        comandos_Rohde.Presets_Inicial(2441,3,30,30,"MAXH")
        time.sleep(5)
        #Delt01 = "CALC:MARK1:MAX"
        #Delt02 = "CALC:DELT1:MAX:NEXT"
        #Delt03 = "CALC:DELT2:MAX:NEXT"
        #
        #instr.write_str(Delt01)
        #time.sleep(2)
        #instr.write_str(Delt02)
        #time.sleep(2)
        #instr.write_str(Delt03)
        #
        #time.sleep(5)
        #
        #instr.write_str("CALC:MARK1 OFF")
        #instr.write_str("CALC:MARK2 OFF")
        #instr.write_str("CALC:MARK3 OFF")


class Espurios:
    def TecB():
        ## =========================== Temp - Connection ===========================
        #resource_string_1 = 'TCPIP::192.168.0.100::INSTR'
        ##resource_string_1 = 'TCPIP0::FSMRX-000000::inst0::INSTR'
        #instr = RsInstrument(resource_string_1,True,False)
        ## =========================== Temp - Connection ===========================



        Pasta_Destino = "C:\\Print" # Pasta de destino dos prints

        

        OP_FREQ_1 = "2402" # MUDA A FREQUENCIA DE OPERA��O DO ENSAIO
        OP_FREQ_2 = "2302" # MUDA A FREQUENCIA DE OPERA��O DO ENSAIO
        OP_FREQ_3 = "2480" # MUDA A FREQUENCIA DE OPERA��O DO ENSAIO
        OP_FREQ_4 = "2580" # MUDA A FREQUENCIA DE OPERA��O DO ENSAIO

        Freq_OP_BaixaA = OP_FREQ_1 # DEFINA A FREQUENCIA DE MOVIMENTACAO DO MARKER 2 PRINT_1
        Freq_OP_BaixaB = "2395" # DEFINA A FREQUENCIA DE MOVIMENTACAO DO MARKER 2 PRINT_2
        Freq_OP_AltaA = OP_FREQ_3  # DEFINA A FREQUENCIA DE MOVIMENTACAO DO MARKER 2 PRINT_3
        Freq_OP_AltaB = "2502"  # DEFINA A FREQUENCIA DE MOVIMENTACAO DO MARKER 2 PRINT_4

        Pick_1_Max = "CALC:MARK1:MAX"         # Comando Marker 1 MAX
        Pick_2_Left = "CALC:MARK2:MAX:LEFT"  # Comando Marker 2 MAX Esquerda
        Pick_2_Righ = "CALC:MARK2:MAX:RIGH"   # Comando Marker 2 MAX Direita

        # ============================== Presets conforme a 14448 ==============================
        RBW = "BAND 100kHz"
        VBW = "BAND:VID 300kHz"
        Ref = "DISP:WIND:TRAC:Y:RLEV 20dBm"
        Att = "INP:ATT 30 DB"
        MaxHold = "DISP:WIND:TRAC:MODE MAXH"
        # ============================== Presets conforme a 14448 ==============================

        # ===================Frequencias===================
        FreqStar_A = "FREQ:STAR 30MHz"
        FreqStop_A = "FREQ:STOP "+OP_FREQ_1+"MHz"

        FreqStar_B = "FREQ:STAR "+OP_FREQ_2+"MHz"
        FreqStop_B = "FREQ:STOP "+OP_FREQ_1+"MHz"

        FreqStar_C = "FREQ:STAR "+OP_FREQ_3+"MHz"
        FreqStop_C = "FREQ:STOP "+OP_FREQ_4+"MHz"

        FreqStar_D = "FREQ:STAR "+OP_FREQ_3+"MHz"
        FreqStop_D = "FREQ:STOP 18GHz"
        # ===================Frequencias===================


        
        # -------------- Envia os Presets para o Instrument --------------
        instr.write_str(RBW)
        instr.write_str(VBW)
        instr.write_str(Ref)
        instr.write_str(Att)
        instr.write_str(MaxHold)
        # -------------- Envia os Presets para o Instrument --------------]

#=================================================== MENSSAGEM_WA ===================================================

        messagebox.showwarning(title="Mudar frequencia!",message="Mude a frequencia do ESE para 2412MHz, Canal 1") 
                                
#=================================================== FREQUENCIA_C ===================================================

        #=================================================== FREQUENCIA_A ===================================================

        instr.write_str("CALC:MARK1 OFF") #Limpa o Marker 1
        instr.write_str("CALC:MARK2 OFF") #Limpa o Marker 2

        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-= Set Frequencia do Ensaio =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        instr.write_str(FreqStar_A)
        instr.write_str(FreqStop_A)
        time.sleep(15)
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-= Set Frequencia do Ensaio =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        # IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII Condicao IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        try:
            instr.write_str(Pick_1_Max)
            instr.write_str(Pick_2_Left)
            instr.query_opc(3000)
        except:
            instr.write_str("CALC:MARK1:MAX")
            time.sleep(3)
            instr.write_str("CALC:MARK2:X "+Freq_OP_BaixaA+"MHz")
            instr.query_opc(3000)
            time.sleep(5)
            try:
                instr.write_str(Pick_2_Left)
                instr.query_opc(3000)
            except:
                print("ERRO_A")
                time.sleep(1)
            print("Printscreen!")
            # --------------------------------- Funcao Print ---------------------------------
            instr.write_str("HCOP:DEV:LANG WMF")
            instr.write_str("MMEM:NAME 'c:\\temp\Screen_A.WMF'")
            instr.write_str("HCOP:IMM")
            instr.query_opc(3000)
            instr.read_file_from_instrument_to_pc("c:\\temp\Screen_A.WMF", Pasta_Destino+"\\"+"\PC_Screen_A.WMF")
            # --------------------------------- Funcao Print ---------------------------------
            time.sleep(3)
        else:
            print("Printscreen!")
            # --------------------------------- Funcao Print ---------------------------------
            instr.write_str("HCOP:DEV:LANG WMF")
            instr.write_str("MMEM:NAME 'c:\\temp\Screen_A.WMF'")
            instr.write_str("HCOP:IMM")
            instr.query_opc(3000)
            instr.read_file_from_instrument_to_pc("c:\\temp\Screen_A.WMF", Pasta_Destino+"\\"+"\PC_Screen_A.WMF")
            # --------------------------------- Funcao Print ---------------------------------
            time.sleep(3)
        # IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII Condicao IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII


        #=================================================== FREQUENCIA B ===================================================
        instr.write_str("CALC:MARK1 OFF")#Limpa o Marker 1
        instr.write_str("CALC:MARK2 OFF")#Limpa o Marker 2

        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-= Set Frequencia do Ensaio =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        instr.write_str(FreqStar_B)
        instr.write_str(FreqStop_B)
        time.sleep(15)
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-= Set Frequencia do Ensaio =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        # IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII Condicao IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        try:
            instr.write_str(Pick_1_Max)
            time.sleep(2)
            instr.write_str(Pick_2_Left)
            instr.query_opc(3000)
        except:
            instr.write_str("CALC:MARK1:MAX")
            time.sleep(3)
            instr.write_str("CALC:MARK2:X "+Freq_OP_BaixaB+"MHz")
            instr.query_opc(3000)
            time.sleep(5)
            try:
                instr.write_str(Pick_2_Left)
                instr.query_opc(3000)
            except:
                print("ERRO_B")
                time.sleep(1)
            print("Printscreen!")
            # --------------------------------- Funcao Print ---------------------------------
            instr.write_str("HCOP:DEV:LANG WMF")
            instr.write_str("MMEM:NAME 'c:\\temp\Screen_B.WMF'")
            instr.write_str("HCOP:IMM")
            instr.query_opc(3000)
            instr.read_file_from_instrument_to_pc("c:\\temp\Screen_B.WMF", Pasta_Destino+"\\"+"\PC_Screen_B.WMF")
            # --------------------------------- Funcao Print ---------------------------------
            time.sleep(3)
        else:
            print("Printscreen!")
            # --------------------------------- Funcao Print ---------------------------------
            instr.write_str("HCOP:DEV:LANG WMF")
            instr.write_str("MMEM:NAME 'c:\\temp\Screen_B.WMF'")
            instr.write_str("HCOP:IMM")
            instr.query_opc(3000)
            instr.read_file_from_instrument_to_pc("c:\\temp\Screen_B.WMF", Pasta_Destino+"\\"+"\PC_Screen_B.WMF")
            # --------------------------------- Funcao Print ---------------------------------
            time.sleep(3)
        # IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII Condicao IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII


#=================================================== MENSSAGEM_WA ===================================================

        messagebox.showwarning(title="Mudar frequencia!",message="Mude a frequencia do ESE para 2462MHz, Canal 11") 
                                
#=================================================== FREQUENCIA_C ===================================================
        
        
        
        instr.write_str("CALC:MARK1 OFF")#Limpa o Marker 1
        instr.write_str("CALC:MARK2 OFF")#Limpa o Marker 2

        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-= Set Frequencia do Ensaio =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        instr.write_str(FreqStar_C)
        instr.write_str(FreqStop_C)
        time.sleep(15)
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-= Set Frequencia do Ensaio =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        # IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII Condicao IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        try:
            instr.write_str(Pick_1_Max)
            instr.write_str(Pick_2_Righ)
            instr.query_opc(3000)
        except:
            instr.write_str("CALC:MARK1:MAX")
            time.sleep(3)
            instr.write_str("CALC:MARK2:X "+Freq_OP_AltaB+"MHz")
            instr.query_opc(3000)
            time.sleep(5)
            try:
                instr.write_str(Pick_2_Righ)
                instr.query_opc(3000)
            except:
                print("ERRO_C")
                time.sleep(1)
            print("Printscreen!")
            # --------------------------------- Funcao Print ---------------------------------
            instr.write_str("HCOP:DEV:LANG WMF")
            instr.write_str("MMEM:NAME 'c:\\temp\Screen_C.WMF'")
            instr.write_str("HCOP:IMM")
            instr.query_opc(3000)
            instr.read_file_from_instrument_to_pc("c:\\temp\Screen_C.WMF", Pasta_Destino+"\\"+"\PC_Screen_C.WMF")
            # --------------------------------- Funcao Print ---------------------------------
            time.sleep(3)
        else:
            print("Printscreen!")
            # --------------------------------- Funcao Print ---------------------------------
            instr.write_str("HCOP:DEV:LANG WMF")
            instr.write_str("MMEM:NAME 'c:\\temp\Screen_C.WMF'")
            instr.write_str("HCOP:IMM")
            instr.query_opc(3000)
            instr.read_file_from_instrument_to_pc("c:\\temp\Screen_C.WMF", Pasta_Destino+"\\"+"\PC_Screen_C.WMF")
            # --------------------------------- Funcao Print ---------------------------------
            time.sleep(3)
        # IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII Condicao IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

        #=================================================== FREQUENCIA_D ===================================================
        instr.write_str("CALC:MARK1 OFF")#Limpa o Marker 1
        instr.write_str("CALC:MARK2 OFF")#Limpa o Marker 2

        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-= Set Frequencia do Ensaio =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        instr.write_str(FreqStar_D)
        instr.write_str(FreqStop_D)
        time.sleep(15)
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-= Set Frequencia do Ensaio =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        # IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII Condicao IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        try:
            instr.write_str(Pick_1_Max)
            instr.write_str(Pick_2_Righ)
            instr.query_opc(3000)
        except:
            instr.write_str(Pick_1_Max)
            time.sleep(3)
            instr.write_str("CALC:MARK2:X "+Freq_OP_AltaA+"MHz")
            instr.query_opc(3000)
            time.sleep(5)
            try:
                instr.write_str(Pick_2_Righ)
                instr.query_opc(3000)
            except:
                print("ERRO_D")
                time.sleep(1)
            print("Printscreen!")
            # --------------------------------- Funcao Print ---------------------------------
            instr.write_str("HCOP:DEV:LANG WMF")
            instr.write_str("MMEM:NAME 'c:\\temp\Screen_D.WMF'")
            instr.write_str("HCOP:IMM")
            instr.query_opc(3000)
            instr.read_file_from_instrument_to_pc("c:\\temp\Screen_D.WMF", Pasta_Destino+"\\"+"\PC_Screen_D.WMF")
            # --------------------------------- Funcao Print ---------------------------------
            time.sleep(3)
        else:
            print("Printscreen!")
            # --------------------------------- Funcao Print ---------------------------------
            instr.write_str("HCOP:DEV:LANG WMF")
            instr.write_str("MMEM:NAME 'c:\\temp\Screen_D.WMF'")
            instr.write_str("HCOP:IMM")
            instr.query_opc(3000)
            instr.read_file_from_instrument_to_pc("c:\\temp\Screen_D.WMF", Pasta_Destino+"\\"+"\PC_Screen_D.WMF")
            # --------------------------------- Funcao Print ---------------------------------
            time.sleep(3)
        # IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII Condicao IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

        #=================================================== MENSSAGEM_WA ===================================================

        messagebox.showinfo(title="Ensaio Finalizado",message="O ensaio Foi finalizado! Aperte OK para continuar...")

class Funcoes:
    def Prints():

        Pasta_Destino = "C:\\Print"
        instr.write_str("HCOP:DEV:LANG WMF")
        instr.write_str("MMEM:NAME 'c:\\temp\Screen_ANALOG.WMF'")
        instr.write_str("HCOP:IMM")
        instr.query_opc(3000)
        instr.read_file_from_instrument_to_pc("c:\\temp\Screen_ANALOG.WMF", Pasta_Destino+"\\"+"\EDR-3DH1-8DPSK.WMF")


#Ensaios_temp.Separacao_de_Canais_de_Salto()
#Espurios.TecB()
#time.sleep(15)
Funcoes.Prints()