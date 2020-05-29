# * ปิด NUMLOCK ทุกครั้งก่อนการ run (Bug ของ Sukili ทำให้กด Shift ค้างไม่ได้)

import datetime

# Settings
roundRun = 246 # จำนวนไอเทม จำนวนรอบที่โปรแกรมต้องทำงาน
savePath = "C:\\MBR-2\\110301790101\\" # Path ที่เก็บโฟลเดอร์และไฟล์

start = time.time() # เวลาที่เริ่มโปรแกรม

for m in range(roundRun):
    # Click หน้าจอ Production Report ให้อยู่ด้านหน้าตัวเลข MO no. (บรรทัดแรก)
    click(Region(1466,375,145,9))
    
    # Select MO no.
    for n in range(8):
        type(Key.RIGHT , KeyModifier.SHIFT)
    
    # Copy MO no.
    type("c", KeyModifier.CTRL)
    
    # Click ปุ่ม Filter หน้าจอ Manufacturing orders
    #click(Region(1636,155,15,16))
    
    # Click Textbox หน้าจอ Filter Manufacturing orders
    click(Region(2690,85,40,13))
    
    # ลบข้อมูลใน Textbox ทิ้ง
    for n in range(20):
        type(Key.BACKSPACE)
    
    # วางข้อมูล MO no. ที่ Copy ไว้
    type("v", KeyModifier.CTRL)
    
    # กดปุ่ม Apply
    click(Region(2581,488,65,18))
    
    # double click ที่หน้าจอ Manufactureing orders เพื่อเปิดหน้าจอรายละเอียด
    sleep(1)
    doubleClick(Region(352,392,11,6))
    
    # Click ที่ Textbox Batch
    sleep(1)
    click(Region(641,326,1,10))
    
    # Select Batch
    for n in range(8):
        type(Key.RIGHT , KeyModifier.SHIFT)
        
    # Copy Batch no
    type("c", KeyModifier.CTRL)
    
    # Close หน้าจอรายละเอียด
    click(Region(899,200,27,11))
    
    # Click Active หน้าจอ windows folder
    click(Region(989,557,27,17))
    
    # สร้าง Folder ใหม่
    type("n", KeyModifier.CTRL + KeyModifier.SHIFT)
    sleep(1)
    # Paste Batch no เพื่อตั้งเป็นชื่อ Folder
    type("v", KeyModifier.CTRL)
    sleep(1)
    type(Key.ENTER)
    
    # Enter เข้า Folder
    #type(Key.ENTER)
    
    # หน้าจอ Manufactureing orders Click menu Table --> Print
    click(Region(1517,394,34,15))
    sleep(1)
    for n in range(5):
        type(Key.DOWN)
    type(Key.ENTER)

    # รอหน้า Popup Print ขึ้น
    sleep(4)

    # Click จอ Print ให้ Active
    click(Region(1978,415,112,20))
    
    # กดเลือก Layout
    type(Key.DOWN)
    
    # เปลี่ยน Print Server
    type(Key.TAB)
    for n in range(27):
        type(Key.DOWN)
    
    # เปลี่ยน Printer
    type(Key.TAB)
    for n in range(18):
        type(Key.DOWN)
    
    # Click ปุ่ม Print
    click(Region(2199,454,43,14))
    
    # Wait Windows Popup
    #wait(Pattern("pdfcreator_title.png").similar(0.80),)
    doWhile = True # while loop
    counter = 1 # loop counter
    firstLoop = True # first loop checker

    sleep(80)

    if exists("pdfcreator_monitor.png"):
        click("pdfcreator_monitor.png")
        type(Key.F2)
    
    while doWhile:
        sleep(1)

        if firstLoop: # Loop แรกตั้งค่า timeout 1 ชั่วโมง เพื่อรอการประมวลผลไฟล์ PDF
            timeOut = 3600
        else: # Loop ต่อไปให้รอ 3 วินาที
            timeOut = 3

        # ตรวจสอบว่ามี หน้าจอของ PDFCreator 1.2.3 ขึ้นมาหรือยัง
        if exists(Pattern("pdfcreator_document.png").exact(), timeOut):
            click(Pattern("pdfcreator_document.png").exact()) # Click Title เพื่อ Active หน้าจอ
            sleep(1)
            click(Region(864,273,25,9)) # click textbox
            type(str(counter)) # พิมพ์ชื่อไฟล์ (ใช้ตัวแปร counter)
            click(Region(894,644,64,17)) # Click ปุ่ม Save (หน้าจอ PDFCreator)
            sleep(1)
            if (firstLoop): # ถ้าเป็นการ save ครั้งแรกให้ใส่ path
                click(Region(969,363,40,26))
                type(Key.F4) # คีย์ลัดเปลี่ยน path ที่จะ save
                type("a", KeyModifier.CTRL) # select all (Ctrl+a)
                type(savePath) # พิมพ์ path (eg. C:\Users\gpo\Desktop\MBR\)
                type("v", KeyModifier.CTRL) # วาง Batch ต่อท้าย path (eg. M603793)
                type(Key.ENTER) # กดปุ่ม Enter เพื่อเปลี่ยน path
            click("windows_save_button.png") # Click ปุ่ม Save (หน้าจอ save dialog)
        else:
            doWhile = False # ถ้าไม่เจอหน้าจอภายในระยะเวลาที่กำหนด ให้ออกจาก Loop
        
        counter += 1
        firstLoop = False
    
    # ปิด popup print
    sleep(2)
    click(Region(1408,527,14,13))

    sleep(1)
    click(Region(1522,367,21,18)) # Click หน้าจอ Production Report
    type(Key.DOWN) # เลื่อนลง 1 บรรทัด
    #click(Region(1167,682,14,13)) # Click ที่ ปุ่ม Down Scroll

done = time.time() # เวลาที่โปรแกรมรันเสร็จ
elapsed = done - start # คำนวณเวลาที่โปรแกรมใช้รัน
timeuse = str(datetime.timedelta(seconds=round(elapsed))) # เวลาที่ใช้ format hh:mm:ss

# แสดง ข้อความแจ้งรันโปรแกรมเสร็จแล้ว
popup("Finished - %s" % timeuse )

# Debug Only
#print "Clipboard[%s]" % Env.getClipboard()
