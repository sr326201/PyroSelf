3
œO^�I  �               @   s�  d dl mZmZmZmZmZ d dlmZmZ d dl	m
Z
 d dlZd dlZd dlZd dlZd dlZd dl	Z	d dlZd dlZd dlmZ d dlmZ d dlmZ d dlT d d	lmZ e� Zejd
�r�ejd� nRed�Zed�Zed�Zed�Zeeeed�ed< e dd��Z!ej"e!� W dQ R X ed d Zed d Zed d ZdQZ#dZ$dZ%dZ&edee�Z'e	j
dddddd �Z(dZ)ej*� Z+ej*� Z,e,e+ j-d! Z.d"d#d$d%d&d'd(d)d*d+d,d-j/e.�gZ0d.d/� Z1d0d1� Z2d2d3� Z3d4d5� Z4d6d7� Z5e'j6ej7ej8e$�@ �d8d9� �Z9e'j6ej:d:d;�ej;@ �d<d:� �Z<e'j6ej:d=d;�ej;@ �d>d?� �Z=e'j6ej:d@d;�ej;@ �dAdB� �Z>e'j6ej:dCd;�ej;@ �dDdE� �Z?e'j6ej7ddF�dGdH� �Z@e'j6ej7dIdF�dJdK� �ZAe'j6ej:dLd;�ej;@ �dMdN� �ZBe'j6� dOdP� �ZCe'jD�  dS )R�    )�Client�Message�Filters�Chat�InputPhoneContact)�	functions�types)�StrictRedisN)�path)�sleep)�datetime)�*)�ConfigParserz./config.iniz
config.inizPlease Send Api-Id : zPlease Send Api-Hash : zPlease Send User-Id Sudo : zPlease Send User-Id log : )�api_id�api_hash�sudo�gplogz	Pyro-Self�wr   r   r   �*https://github.com/attavakoli/PyroSelf.git�masteri(� g      �?u   
❂New update 2020

✇New commands :

1 - setbio
2 - setnew
3 - ecoe
4 - upgrade

✇Fix all bug✇

#By @Salazar & @Sigaris
Z	localhosti�  �   zUTF-8T)�hostZportZdb�charsetZdecode_responsesi�  z           %00u   █          %10u   ██         %20u   ███        %30u   ████       %40u   █████      %50u   ██████     %60u   ███████    %70u   ████████   %80u    █████████  %90u#   ██████████ %100zReload! {} msc             C   s*   t d d jd�}t| �|kr"dS dS d S )Nz	Pyro-Selfr   �,TF)�config�split�str)�user_idZ
sudo_users� r   �self.py�SUDOD   s    r    c             C   s    d}t jdt| � |�rd}|S )NFzself:muteallT)�database�	sismemberr   )�chat_idr   �varr   r   r   �muteallK   s    r%   c             C   s"   g }x| D ]}|j |j� q
W |S )N)�append�
message_id)Zmsg_listZlist_ids�msgr   r   r   �get_idsQ   s    
r)   c             C   s   | j ||� d S )N)�delete_messages)�appr#   Zmsg_idsr   r   r   �delmsgW   s    r,   c             C   s|   | j dd�} | j dd�} | j dd�} | j dd�} | j d	d
�} | j dd�} | j dd�} | j dd�} | j dd�} | j dd�} | S )N�0u   0️⃣�1u   1️⃣�2u   2️⃣�3u   3️⃣�4u   4️⃣�5u   5️⃣�6u   6️⃣�7u   7️⃣�8u   8️⃣�9u   9️⃣)�replace)r(   r   r   r   �	number_toZ   s    r8   c             C   s   t |� d S )N)�print)�client�messager   r   r   �pv_telegramg   s    r<   �upgrade� c             C   sx   |j d�}tjd� tjd�}|j d|� �� tjd� |j dt� dt� �� tjd� tjt	j
t	j
ft	j��  t`d S )	Nz~ Updating robot please wait...�   z:git pull https://github.com/attavakoli/PyroSelf.git masterz ~ Applying update changes... 

 �   zq~ The latest version of gitHub has been downloaded and implemented and the robot is ready to work! 

~ version : z 
 r   )�edit�timer   �
subprocessZgetstatusoutput�sversion�newup�os�execl�sys�
executable�argv�	threadingZThread)r:   r;   �a�outr   r   r   r=   k   s    




Zsetnamec             C   sH   t tj� k rDdj|jdd � �}tjtjj|d�� |j	dj
|�� d S )N� r   )�
first_namez*~ Name changed succesfully! 

 ~ name : {})�	sleeptimerB   �join�commandr+   �sendr   �account�UpdateProfilerA   �format)r:   r;   �namer   r   r   �set_namew   s    rX   Zsetprofc             C   s<   |j r|j j� }n|j� }tj|� |jd� tj|� d S )Nz"~ Profile Picture Set Succesfully!)�reply_to_message�downloadr+   Zset_profile_photorA   rF   �remove)r:   r;   �picr   r   r   �set_profile_pic~   s    

r]   Zsetbioc             C   s`   t tj� k r\dj|jdd � �}t|�dkr8|jd� n$| jtjj	|d�� |jdj
|�� d S )NrN   r   �F   z%~ Bio too long maximum 70 characters!)Zaboutz(~ Bio succesfully changed! 

 ~ bio : {})rP   rB   rQ   rR   �lenrA   rS   r   rT   rU   rV   )r:   r;   Zbior   r   r   �set_bio�   s    r`   )�groupc          	   C   sh   yNt j� }|j}tjd�}|dkrL|dkrLtjd�p6d}t j|jj|� qLn W n   td� Y nX d S )Nzmonshi-mode�offline�onz
self:mtextz*User is offline please send message later!rN   )	r+   �get_me�statusr!   �get�send_message�chat�idr9   )r:   r;   �mere   �monshi�txtr   r   r   rb   �   s    
rb   r?   c             C   s$   t jd�}|dkr tj|jj� d S )Nzself:markreadallrc   )r!   rf   r+   Zread_historyrh   ri   )r:   r;   �markreadr   r   r   rm   �   s    
rm   Zecoec             C   s|   ybd}|j jdd�d }|jd�}x<|D ]4}||7 }|jd|� d��}|jd|j� � d��}q(W W n   td� Y nX d S )Nr>   rN   r   z`|`�`z|`)�textr   rA   �stripr9   )r:   r;   Zchrl   Zms�ir   r   r   ro   �   s    

ro   c          �  C   s:  y4t jd|jj�r2|jdkr2t|jj�s2|jd� W n4 tk
rh } zt	j
tdj|�� W Y d d }~X nX y(t jd|jj�r�|r�t	j|jjd� W n4 tk
r� } zt	j
tdj|�� W Y d d }~X nX yT|jdk�rt	j|jjdd	�d
 }t	j|jj|j|jdj|jj|jj|jj�� W n6 tk
�rR } zt	j
tdj|�� W Y d d }~X nX y|jdk�rl|jd� W n6 tk
�r� } zt	j
tdj|�� W Y d d }~X nX t|jj��r�|jdk�r�|j�r�|j�  |jj� }t	jt|� tj|� yB|jdk�r0|j�r0|jjj}|jdj|�� t	j|jj|� W n6 tk
�rh } zt	j
tdj|�� W Y d d }~X nX y<|jdk�r�|j�r�|jjj}t	j|� |jdj|�� W n6 tk
�r� } zt	j
tdj|�� W Y d d }~X nX y<|jdk�r|j�r|jjj}t	j|� |jdj|�� W n6 tk
�rP } zt	j
tdj|�� W Y d d }~X nX yN|jdk�r�x"tD ]}t	j|jj|j|� �qfW t j!}tj"||ft j#��  W n6 tk
�r� } zt	j
tdj|�� W Y d d }~X nX yJ|jdk�r |j�r |jjj}|jdj|�� t j$dt%|jj� |� W n6 tk
�rX } zt	j
tdj|�� W Y d d }~X nX yJ|jd k�r�|j�r�|jjj}|jd!j|�� t j&dt%|jj� |� W n6 tk
�r� } zt	j
td"j|�� W Y d d }~X nX y�|jd#k�r\t j'dt%|jj� �t(d
�k�r|jd$� nFd%}x0t j)dt%|jj� �D ]}|d&j||�7 }�q2W |j|d'd(d)� W n6 tk
�r� } zt	j
td*j|�� W Y d d }~X nX y�|j�rHt*j+d+|j��rH|jj,dd,�}	t(|	�}|jjj}t jdt%|jj� |��r�|jd-� nR|jd.j||	�� t j$dt%|jj� |� |d/ }
t-|
� t j&dt%|jj� |� W n6 tk
�r� } zt	j
td0j|�� W Y d d }~X nX yL|jd1k�r�t j.d2�d3k�r�t j/d2d4� d5}	nt j/d2d3� d6}	|j|	� W n6 tk
�r } zt	j
td7j|�� W Y d d }~X nX yF|j�rJt*j+d8|j��rJ|jj,d9d,�}	|jd:j|	�� t j/d;|	� W n6 tk
�r� } zt	j
td<j|�� W Y d d }~X nX y$|jd=k�r�|jd>� t jd;� W n6 tk
�r� } zt	j
td?j|�� W Y d d }~X nX y(|jd@k�r|jdA� t	j0|jj� W n6 tk
�r> } zt	j
tdBj|�� W Y d d }~X nX yH|jdCk�r�t jd|jj��rl|jdD� n|jdE� t j$d|jj� W n6 tk
�r� } zt	j
tdFj|�� W Y d d }~X nX y*|jdGk�r�|jdH� t j&d|jj� W n6 tk
�	r  } zt	j
tdIj|�� W Y d d }~X nX y&|jdJk�	s<|jdKk�	rF|jdL� W n6 tk
�	r~ } zt	j
tdMj|�� W Y d d }~X nX y�|j�
r@t*j+dN|j��
r@|jj,dNd,�}	|jdO� t-dP� |jdQ� t-dP� |jdR� t-dP� |jdS� t-dP� |jdT� t-dP� dU}x8|	D ]0}t1t%|��}|dVj|�7 }|jdWj|�� �
qW W n6 tk
�
rx } zt	j
tdXj|�� W Y d d }~X nX y(|jdYk�
r�t	j2� }|jdZj|�� W n6 tk
�
r� } zt	j
td[j|�� W Y d d }~X nX y8|jd\k�r|j�rt	j3|jjj�}|jdZj|�� W n6 tk
�rH } zt	j
td]j|�� W Y d d }~X nX yT|jd^k�sd|jd_k�r�|jj}t	j2� }t	j4|jj|j� t	j5|jj|j6|j� W n6 tk
�r� } zt	j
td`j|�� W Y d d }~X nX y�|jdak�rxt	j7|jj�}|db } x<t8| �D ]0}t9t	|jjt:t	j;|jjdb��� t<j-dc� �qW t9t	|jjt:t	j;|jj|| db  ��� |j�  t	j
|jjdd� W n6 tk
�r� } zt	j
tdej|�� W Y d d }~X nX yF|jdfk�r�t=j>� }t?j@� }|jdgj|jA|jB|jC|jD|jE|jF�� W n6 tk
�r. } zt	j
tdhj|�� W Y d d }~X nX yH|jdik�rvt jd|jj��r\|jdj� n|jdk� t j$d|jj� W n6 tk
�r� } zt	j
tdlj|�� W Y d d }~X nX y*|jdmk�r�|jdn� t j&d|jj� W n6 tk
�r } zt	j
tdoj|�� W Y d d }~X nX y6|jdpk�rF|j�rF|jdq� t	jG|jj|jj� W n6 tk
�r~ } zt	j
tdrj|�� W Y d d }~X nX y�|jdsk�s�|jdtk�r>t	j2� }t jd|jj��r�du}ndv}t jd|jj��r�du}ndv}t jdw|j��r�du}ndv}t j.d2�d3k�r
du}ndv}|jdxj|j|j|j||||t j)d;��p8dy�� W n6 tk
�rv } zt	j
tdhj|�� W Y d d }~X nX y(|jdzk�r�t j/dwd3��r�|jd{� W n6 tk
�r� } zt	j
td|j|�� W Y d d }~X nX y&|jd}k�r�|jd~� t j/dwd4� W n6 tk
�r4 } zt	j
tdj|�� W Y d d }~X nX yf|jd�k�sP|jd�k�r�|jj}|j�r�|j|jj|jd�� t	jHtIt%|jjJj6�t%|jjJj��g� W n6 tk
�r� } zt	j
td�j|�� W Y d d }~X nX y*tK|jj|jj��r�t	j4|jj|j� W n6 tk
�r4 } zt	j
td�j|�� W Y d d }~X nX d S )�Nz
self:pokeru   😐z #self 
 #poker 
 {}zself:typingZtypingz #self 
 #typing action 
 {}ri   r   )�limitr   uo   ایدی عددی شما : [ {} ] 
 
 نام اکانت شما : [ {} ] 
 
 نام کاربری شما: [ @{} ]z #self 
 #id 
 {}�selfz.Hi 
 I Am Alireza 
 this Is my Self 
 @Salazarz #self 
 #information : 
 {}zp i cZkickz ~ User {} Kicked This Chat!z #self 
 #kick : 
 {}�blockz ~ User {} Blocked!z #self 
 #block : 
 {}Zunblockz ~ User {} Unblocked!z #self 
 #unblock : 
 {}�reloadz #self 
 #reload : 
 {}Zmutez+ ~ User {} Added Too The Mute List On Self!zself:muteallz #self 
 #mute : 
 {}Zunmutez) ~ User {} Removed The Mute List On Self!z #self 
 #unmute : 
 {}Zmutelistz~ Mute List Is Empty!z~ Mute List: 
z2 ------ <a href='tg://user?id={}'>{}</a> ------ 
 ZHTMLT)Z
parse_modeZdisable_web_page_previewz #self 
 #mutelist : 
 {}zmute r>   z(~ This User is already in the Mute list!z6~ User [ {} ] Added To The Mutelist For [ {} ] Minute!�<   z #self 
 #mute min : 
 {}rk   zmonshi-moderc   ZoffzSelf Monshi Is OffzSelf Monshi Is On!z #self 
 #monshi off : 
 {}z
setmonshi Z	setmonshiz~ Text [ {} ] Seted For Monshi!z
self:mtextz #self 
 #monshitext : 
 {}Zcleanmonshitextz~ Monshi Text Is Deleted!z  #self 
 #cleanmonshitext : 
 {}Zleavez~ Bye!z #self 
 #leave : 
 {}zpoker onz~ Poker Mode Already On!z~ Poker Mode Is Activited!z #self 
 #poker on : 
 {}z	poker offz~ Poker Mode Is Deactived!z #self 
 #poker off : 
 {}ZHelp�helpa  ~ GIOUTiN Self Help: 
 
 
 [ self ] : For information! 
 
 [ stats ] : Information Your Account! 
 
 [ kick ] : Ban a User (For Supergroups)! 
 
 [ block | unblock ] : Block a User! 
 
 [ reload ] : Reload & Check The Source! 
 
 [ mute | unmute ] : Silent The User (For Supergroups)! 
 
 [ mutelist ] : Get a list Silents User in Supergroup! 
 
 [ mute x ] : Mute a person in a timed manner(Just Reply|Replace the number of minutes you want to be in Mute instead of [x]! example : mute 5) 
 
 [ Share ] : Share Your Contact! 
 
 [ Addc ] : Add The Share Contacts! 
 
 [ setprof ]: Reply To Picture Then Setted Picture On Your Profile!
 
 [ monshi on|monshi off ]: Turn On|Off The Monshi!
 
 [ setmonshi text|cleanmonshitext ]: Set And Delete Text Monshi!(Replace Your Monshi Text In [text])
 
 [ id ] : Your information! 
 
 [ markreadall on|markreadall off ] : Active & Deactive Markread In All Chats!
 
 [ cleanmsgs ] : Clean All Message In Supergroups! 
 
 [ typing on|typing off ] : Active & Deactive Typing Action In One Supergroup! 
 
 [ poker on|poker off ] : Active & Deactive Poker Mode In One Supergroup! 
 
 [ leave ] : Left The Chat! 
 
 [ pin ] : Pin A Message In Supergroup! 
 
 [ time ] : For Fun! 
 
 
 ---- ~ Coder : @Salazar ---- 
 ---- ~ Channel : @GIOUTiN ----z #self 
 #Help : 
 {}zincode u   ~ Your String Is Incoding 🌑r?   u   ~ Your String Is Incoding 🌒u   ~ Your String Is Incoding 🌓u   ~ Your String Is Incoding 🌔u   ~ Your String Is Incoding 🌕z~ Your String Is Incoded : 
 z{}	z{}z #self 
 #incoding : 
 {}Zgetmez~ This is Answer : 
 
 {}z #self 
 #GetMe : 
 {}Zgetuserz #self 
 #Getuser : 
 {}ZshareZSharez #self 
 #share : 
 {}Z	cleanmsgs�c   g333333�?z~ All Chats Cleared!z #self 
 #cleanmsgs : 
 {}rB   z�~ Time : [ {}:{}:{} ] 
 ~ Year: [ {} ] 
 ~ Month : [ {} ] 
 ~ Day : [ {} ] 
 
 ~ Coder: @Salazar 
 ~ Channel : @GIOUTiN & @Pinigerteamz #self 
 #session : 
 {}z	typing onz~ Typing Action Is Already On!z"~ Typing Action Activited This Gp!z! #self 
 #typing on one gp : 
 {}z
typing offz%~ Typing Action Is Deactived This Gp!z" #self 
 #typing off one gp : 
 {}Zpinz~ This Message Is Pinned!z #self 
 #pin : 
 {}ZstatsZStatsu   ✔️u   ❌zself:markreadalluG  ~ Your Account Information: 
 
 
 • Name: [ {} ] 
 
 • Username: [ {} ] 
 
 • Userid: [ {} ] 
 
 • Typing In This Gp: [ {} ] 
 
 • Poker In This Gp: [ {} ] 
 
 • Markread In All Spgs & PV: [ {} ] 
 
 • Monshi Action: [ {} ] 
 
 • Monshi Text: [ {} ] 
 
 
 ~ Coder: @Salazar 
 ~ Channel : @GIOUTiN & @Pinigerteamz*User is offline please send message later!zmarkreadall onz~ Markread All Is Activited!z #self 
 #markreadall on : 
 {}zmarkreadall offz~ Markread All Is Deactived!z  #self 
 #markreadall off : 
 {}ZaddcZAddcz!~ This Number Added Too Contacts!z #self 
 #addcontact : 
 {}z #self 
 #delmute : 
 {})Lr!   r"   rh   ri   ro   r    Z	from_userZ
reply_text�	Exceptionr+   rg   r   rV   Zsend_chat_actionZget_profile_photosZ
send_photoZfile_idZfile_refrO   ZusernamerY   �deleterZ   rF   r[   rA   Zkick_chat_memberZ
block_userZunblock_user�reloadlZedit_message_textr'   rH   rI   rG   rJ   Zsaddr   ZsremZscard�intZsmembers�re�searchr7   r   rf   �setZ
leave_chat�ordrd   Z	get_usersr*   Zsend_contactZphone_numberZget_history_count�ranger,   r)   Zget_historyrB   r   �nowZ
JalaliDateZtodayZhourZminute�secondZyearZmonthZdayZpin_chat_messageZadd_contactsr   Zcontactr%   )�cr;   �er\   Zidsrq   �pythonro   �allrl   �min�bZmy�userZmyidZall_msgZtmZjdate�typZpkrZmrkallZmnshr   r   r   �cmd�   s&   
$$2$$


$

$

$
$
$
$ $
$$$
$
$
$
$$





$$$$ ($*$
$
$
$4$$
$*$r�   )r   r   )EZpyrogramr   r   r   r   r   Zpyrogram.apir   r   Zredisr	   rF   rH   Zrequestsr}   rB   rC   rK   r
   r   r   Zkhayyam�configparserr   r   �isfile�read�inputr   r   r   r   �openZ
configfile�writeZgitpullZtelegramrD   rE   r+   r!   rP   r�   Z	starttimeZendtimeZmicrosecondsZmstimerV   r{   r    r%   r)   r,   r8   Z
on_messageZprivater�   r<   rR   rj   r=   rX   r]   r`   rb   rm   ro   r�   Zrunr   r   r   r   �<module>   s~   @
   
 
   R