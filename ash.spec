# conditional build
# --without static
# --with dietlibc (link with dietlibc, implies --without static)
# Branch: HEAD

%{?_with_dietlibc:%define _without_static 1}

Summary:	Small bourne shell from Berkeley
Summary(de):	Kleine Bourne-Shell von Berkeley
Summary(fr):	Shell Bourne r�duit de Berkeley
Summary(pl):	Ma�y shell bourne'a
Summary(ru):	����������� ������ Bourne shell (sh)
Summary(tr):	Ufak bir bourne kabu�u
Summary(uk):	��������� ���Ӧ� Bourne shell (sh)
Name:		ash
Version:	0.4.0
Release:	8
License:	BSD
Group:		Applications/Shells
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-builtin.patch
Patch1:		%{name}-echo.patch
Patch2:		%{name}-getcwd.patch
Patch3:		%{name}-getopt.patch
Patch4:		%{name}-glob.patch
Patch5:		%{name}-jobs.patch
Patch6:		%{name}-kill.patch
Patch7:		%{name}-makefile.patch
Patch8:		%{name}-manpage.patch
Patch9:		%{name}-hetio.patch
Patch10:	%{name}-memout.patch
Patch11:	%{name}-misc.patch
Patch12:	%{name}-redir.patch
Patch13:	%{name}-setmode.patch
Patch14:	%{name}-syntax.patch
Patch15:	%{name}-test.patch
Patch16:	%{name}-times.patch
Patch17:	%{name}-debian.patch
Patch18:	%{name}-ppid.patch
Patch19:	%{name}-freebsd.patch
Patch20:	%{name}-sighup.patch
%{?_with_dietlibc:Patch21:	%{name}-dietlibc.patch}
PreReq:		fileutils
PreReq:		grep
%{!?_without_static:BuildRequires:	glibc-static}
%{?_with_dietlibc:BuildRequires:	dietlibc-static}
BuildRequires:	flex
BuildRequires:	byacc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	mkinitrd <= 1.7

%define		_bindir		/bin

%description
ash is a bourne shell clone from Berkeley. It supports all of the
standard Bourne shell commands and has the advantage of supporting
them while remaining considerably smaller than bash.

%description -l de
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle
Standard-Bourne-Shell- Befehle unterst�tzt und dennoch erheblich
weniger Platz beansprucht als bash.

%description -l fr
ash est un clone Berkeley du shell Bourne. Il g�re toutes les
commandes standard du shell Bourne et a l'avantage de les g�rer tout
en restant consid�rablement plus petit que bash.

%description -l pl
Ash jest klonem shella Bourne'a z Berkeley. Obs�uguje standardowe
komendy shella Bourne'a i jest mniejszy ni� bash.

%description -l ru
���� - ��� ������� ��������� ���������, ������� �������������� �������
������������, �������� � ���������� ��� ��� ������ ����. Ash - ���
���� Bourne shell (sh) �� ������. Ash ������������ ��� �����������
������� ����� sh, ������ ����������� ������ ��� sh. � ash �����������
��������� ����������� Bourne shell (��������, ������� ������), �� ��
������� ����������� ������ ������.

%description -l tr
ash, Berkeley'in bir bourne kabu�u kopyas�d�r. Standart bourne kabu�u
komutlar�n�n t�m�n� destekler ve bash kabu�undan daha k���k olma
avantaj�na sahiptir.

%description -l uk
��� - �� ������ �������� ��������, ����� ���������դ �������
�����������, �˦ ��������� � ���צ����� ��� �� ��������� ��ۦ. Ash -
�� ���� Bourne shell (sh) � ����̦. Ash Ц�����դ �Ӧ ��������Φ
������� ���� sh, ������ ������ ������ Φ� sh. � ash צ����Φ ���˦
��������Ԧ Bourne shell (���������, ����Ҧ� ������), ���� צ� �������
������ ����� ���'�Ԧ.

%package static
Summary:	Small bourne shell from Berkeley
Summary(de):	Kleine Bourne-Shell von Berkeley
Summary(fr):	Shell Bourne r�duit de Berkeley
Summary(pl):	Ma�y shell bourne'a
Summary(tr):	Ufak bir bourne kabu�u
Group:		Applications/Shells
PreReq:		fileutils
PreReq:		grep
Conflicts:	mkinitrd <= 1.7

%description static
ash is a bourne shell clone from Berkeley. It supports all of the
standard Bourne shell commands and has the advantage of supporting
them while remaining considerably smaller than bash.

%description static -l de
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle
Standard-Bourne-Shell- Befehle unterst�tzt und dennoch erheblich
weniger Platz beansprucht als bash.

%description static -l fr
ash est un clone Berkeley du shell Bourne. Il g�re toutes les
commandes standard du shell Bourne et a l'avantage de les g�rer tout
en restant consid�rablement plus petit que bash.

%description static -l pl
Ash jest klonem shella Bourne'a z Berkeley. Obs�uguje standardowe
komendy shella Bourne'a i jest mniejszy ni� bash.

%description static -l tr
ash, Berkeley'in bir bourne kabu�u kopyas�d�r. Standart bourne kabu�u
komutlar�n�n t�m�n� destekler ve bash kabu�undan daha k���k olma
avantaj�na sahiptir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
# this is mainly for information, maybe add changelog to %doc?
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%{?_with_dietlibc:%patch21 -p1}

%build

%{?_with_dietlibc:%define __cc %{_arch}-dietlibc-gcc}

%{!?_without_static:%{__make} OPT_FLAGS="%{rpmcflags}" LDFLAGS="-static %{rpmldflags}"}
%{!?_without_static:mv -f sh ash.static}
%{__make} OPT_FLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}
install sh $RPM_BUILD_ROOT%{_bindir}/ash
%{!?_without_static:install ash.static $RPM_BUILD_ROOT%{_bindir}/ash.static}
install sh.1 $RPM_BUILD_ROOT%{_mandir}/man1/ash.1
echo ".so ash.1" > $RPM_BUILD_ROOT%{_mandir}/man1/bsh.1
ln -sf ash $RPM_BUILD_ROOT/%{_bindir}/bsh

%post
if [ ! -f /etc/shells ]; then
	echo "%{_bindir}/ash" > /etc/shells
	echo "%{_bindir}/bsh" >> /etc/shells
else
	if ! grep -q '^%{_bindir}/ash$' /etc/shells ; then
		echo "%{_bindir}/ash" >> /etc/shells
	fi
	if ! grep -q '^%{_bindir}/bsh$' /etc/shells ; then
		echo "%{_bindir}/bsh" >> /etc/shells
	fi
fi

%post static
if [ ! -f /etc/shells ]; then
	echo "%{_bindir}/ash.static" >> /etc/shells
else
	if ! grep -q '^%{_bindir}/ash.static$' /etc/shells ; then
		echo "%{_bindir}/ash.static" >> /etc/shells
	fi
fi

%preun
if [ "$1" = 0 ]; then
	grep -v '^%{_bindir}/ash$' /etc/shells | grep -v '^%{_bindir}/bsh$' > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%preun static
if [ "$1" = 0 ]; then
	grep -v '^%{_bindir}/ash\.static$' /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%verifyscript
for n in ash bsh ; do
	echo -n "Looking for $n in /etc/shells... "
	if ! grep -q "^%{_bindir}/${n}\$" /etc/shells ; then
		echo "missing"
		echo "${n} missing from /etc/shells" >&2
	else
		echo "found"
	fi
done

%verifyscript static
echo -n "Looking for ash.static in /etc/shells... "
if ! grep -q '^%{_bindir}/ash\.static$' /etc/shells ; then
	echo "missing"
	echo "ash.static missing from /etc/shells" >&2
else
	echo "found"
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ash
%attr(755,root,root) %{_bindir}/bsh
%{_mandir}/man1/*

%{!?_without_static:%files static}
%{!?_without_static:%defattr(644,root,root,755)}
%{!?_without_static:%attr(755,root,root) %{_bindir}/ash.static}
