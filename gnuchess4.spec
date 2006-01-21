%define		_name	gnuchess
Summary:	Computer chess program
Summary(de):	Computerschachprogramm
Summary(es):	Juego de ajedrez de la GNU
Summary(fr):	Jeu d'échecs
Summary(pl):	Gra w szachy
Summary(pt_BR):	Jogo de xadrez da GNU
Summary(ru):	ûÁÈÍÁÔÎÁÑ ÐÒÏÇÒÁÍÍÁ GNU
Summary(tr):	Bilgisayar satranç oyunu
Summary(uk):	ûÁÈÏ×Á ÐÒÏÇÒÁÍÁ GNU
Name:		gnuchess4
Version:	4.0.pl80
Release:	11
License:	GPL
Group:		Applications/Games
#Source0:	ftp://ftp.gnu.org/pub/gnu/chess/%{name}-%{version}.tar.gz
Source0:	ftp://distfiles.pld-linux.org/by-md5/8/3/833110654ec086b4ace45e037612033e/%{_name}-%{version}.tar.gz
# Source0-md5:	833110654ec086b4ace45e037612033e
Source1:	xchess.png
Source2:	%{_name}.desktop
Patch0:		%{_name}-fhs.patch
Patch1:		%{_name}-ncurses.patch
Patch2:		%{_name}-ac_fixes.patch
Patch3:		%{name}-errno.patch
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.0
Obsoletes:	gnuchess < 5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gnuchess package contains the GNU chess program. By default,
GNUchess uses a curses text-based interface. Alternatively, GNUchess
can be used in conjunction with the xboard user interface and the X
Window System for a graphical chessboard.

%description -l de
Das berühmte GNU-Schachprogramm. Es ist textorientiert, kann aber mit
'xboard' verwendet werden, um X-orientiertes Schach zu spielen.

%description -l es
Este es el famoso programa de ajedrez de GNU. Está basado en texto,
pero puede ser usado en conjunción con xboard para jugar ajedrez
basado en X.

%description -l fr
Le fameux programme de jeu d'échecs de GNU. Il est en mode texte mais
peut être utilisé avec xboard pour y jouer sous X.

%description -l pl
Oto s³awny GNU program szachowy. Jest w trybie tekstowym, ale w
po³±czeniu z xboard mo¿e mieæ interfejs w X Window.

%description -l pt_BR
Este é o famoso programa de xadrez da GNU. É baseado em texto, mas
pode ser usado em conjunção com xboard para jogar xadrez baseado em X.

%description -l ru
ðÁËÅÔ gnuchess ÓÏÄÅÒÖÉÔ ÛÁÈÍÁÔÎÕÀ ÐÒÏÇÒÁÍÍÕ GNU. ðÏ ÕÍÏÌÞÁÎÉÀ GNUchess
ÉÓÐÏÌØÚÕÅÔ ÔÅËÓÔÏ×ÙÊ ÉÎÔÅÒÆÅÊÓ ÎÁ ÏÓÎÏ×Å curses. áÌØÔÅÒÎÁÔÉ×ÎÏ ÏÎÁ
ÍÏÖÅÔ ÉÓÐÏÌØÚÏ×ÁÔØÓÑ × ÓÏÞÅÔÁÎÉÉ Ó xboard, ÏÂÅÓÐÅÞÉ×ÁÀÝÉÍ ÇÒÁÆÉÞÅÓËÉÊ
ÉÎÔÅÒÆÅÊÓ ÐÏÄ X Window System.

%description -l tr
Bu ünlü GNU satranç programýdýr. Metin ekranda çalýþýr ama xboard
programý ile birlikte kullanýlarak X altýnda da oynanabilir.

%description -l uk
ðÁËÅÔ gnuchess Í¦ÓÔÉÔØ ÛÁÈÏ×Õ ÐÒÏÇÒÁÍÕ GNU. úÁ ÕÍÏ×ÞÁÎÎÑÍ GNUchess
×ÉËÏÒÉÓÔÏ×Õ¤ ÔÅËÓÔÏ×ÉÊ ¦ÎÔÅÒÆÅÊÓ ÎÁ ÏÓÎÏ×¦ curses. áÌØÔÅÒÎÁÔÉ×ÎÏ ×ÏÎÁ
ÍÏÖÅ ×ÉËÏÒÉÓÔÏ×Õ×ÁÔÉÓØ Õ ÐÁÒ¦ Ú ÐÒÏÇÒÁÍÏÀ xboard, ÑËÁ ÚÁÂÅÚÐÅÞÕ¤
ÇÒÁÆ¦ÞÎÉÊ ¦ÎÔÅÒÆÅÊÓ Ð¦Ä X Window System.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd src
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/gnuchess,%{_mandir}/man6} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} -C src install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix}

mv $RPM_BUILD_ROOT%{_bindir}/gnuchess{,4}
install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
sed -e 's,gnuchess,gnuchess4,' %{SOURCE2} > $RPM_BUILD_ROOT%{_desktopdir}/xchess4.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_datadir}/games/gnuchess
%{_mandir}/man6/*
