# conditional build:
# if BOOT is defined, build BOOT package too
Summary:	Small bourne shell from Berkeley
Summary(de):	Kleine Bourne-Shell von Berkeley
Summary(fr):	Shell Bourne réduit de Berkeley
Summary(pl):	Ma³y shell bourne'a 
Summary(tr):	Ufak bir bourne kabuðu
Name:		ash
Version:	0.4.0
Release:	1
License:	BSD
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
Source:      	ash-%{version}.tar.gz
Patch0:		ash-builtin.patch
Patch1:		ash-echo.patch
Patch2:		ash-getcwd.patch
Patch3:		ash-getopt.patch
Patch4:		ash-glob.patch
Patch5:		ash-jobs.patch
Patch6:		ash-kill.patch
Patch7:		ash-makefile.patch
Patch8:		ash-manpage.patch
Patch9:		ash-hetio.patch
Patch10:	ash-memout.patch
Patch11:	ash-misc.patch
Patch12:	ash-redir.patch
Patch13:	ash-setmode.patch
Patch14:	ash-syntax.patch
Patch15:	ash-test.patch
Patch16:	ash-times.patch
Patch17:	ash-debian.patch
Patch18:	ash-ppid.patch
Patch19:	ash-freebsd.patch
Prereq:		fileutils
Prereq:		grep
BuildRequires:	glibc-static
%{?BOOT:BuildRequires:	uClibc-devel-BOOT}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	mkinitrd <= 1.7

%define		_bindir		/bin

%description
ash is a bourne shell clone from Berkeley. It supports all of the
standard Bourne shell commands and has the advantage of supporting
them while remaining considerably smaller than bash.

%description -l de
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle
Standard-Bourne-Shell- Befehle unterstützt und dennoch erheblich
weniger Platz beansprucht als bash.

%description -l fr
ash est un clone Berkeley du shell Bourne. Il gère toutes les
commandes standard du shell Bourne et a l'avantage de les gérer tout
en restant considérablement plus petit que bash.

%description -l pl
Ash jest klonem shell'a Bourne'a z Berkeley. Obs³uguje standardowe
komendy shell'a Bourne'a i jest mniejszy ni¿ bash.

%description -l tr
ash, Berkeley'in bir bourne kabuðu kopyasýdýr. Standart bourne kabuðu
komutlarýnýn tümünü destekler ve bash kabuðundan daha küçük olma
avantajýna sahiptir.

%package static
Summary:	Small bourne shell from Berkeley
Summary(de):	Kleine Bourne-Shell von Berkeley
Summary(fr):	Shell Bourne réduit de Berkeley
Summary(pl):	Ma³y shell bourne'a 
Summary(tr):	Ufak bir bourne kabuðu
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
Prereq:		fileutils
Prereq:		grep
Conflicts:	mkinitrd <= 1.7

%description static
ash is a bourne shell clone from Berkeley. It supports all of the
standard Bourne shell commands and has the advantage of supporting
them while remaining considerably smaller than bash.

%description static -l de
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle
Standard-Bourne-Shell- Befehle unterstützt und dennoch erheblich
weniger Platz beansprucht als bash.

%description static -l fr
ash est un clone Berkeley du shell Bourne. Il gère toutes les
commandes standard du shell Bourne et a l'avantage de les gérer tout
en restant considérablement plus petit que bash.

%description static -l pl
Ash jest klonem shell'a Bourne'a z Berkeley. Obs³uguje standardowe
komendy shell'a Bourne'a i jest mniejszy ni¿ bash.

%description static -l tr
ash, Berkeley'in bir bourne kabuðu kopyasýdýr. Standart bourne kabuðu
komutlarýnýn tümünü destekler ve bash kabuðundan daha küçük olma
avantajýna sahiptir.

%if %{?BOOT:1}%{!?BOOT:0}
%package BOOT
Summary:	Small bourne shell from Berkeley
Summary(de):	Kleine Bourne-Shell von Berkeley
Summary(fr):	Shell Bourne réduit de Berkeley
Summary(pl):	Ma³y shell bourne'a 
Summary(tr):	Ufak bir bourne kabuðu
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki

%description BOOT
ash is a bourne shell clone from Berkeley. It supports all of the
standard Bourne shell commands and has the advantage of supporting
them while remaining considerably smaller than bash.
Version for bootdisk

%endif

%prep
%setup -q -n ash-%{version}
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

%build
# BOOT
%if %{?BOOT:1}%{!?BOOT:0}
%{__make} \
	OPT_FLAGS="-I/usr/lib/bootdisk%{_includedir} -Os" \
	LDFLAGS="-nostdlib -s" \
	LDLIBS="%{_libdir}/bootdisk%{_libdir}/crt0.o %{_libdir}/bootdisk%{_libdir}/libc.a -lgcc"
mv -f sh ash.BOOT
%{__make} clean
%endif

# other
%{__make} OPT_FLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" \
	LDFLAGS="-static %{!?debug:-s}"
mv -f sh ash.static
%{__make} OPT_FLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" \
	LDFLAGS="%{!?debug:-s}"



%install
rm -rf $RPM_BUILD_ROOT

# BOOT
%if %{?BOOT:1}%{!?BOOT:0}
install -d $RPM_BUILD_ROOT/usr/lib/bootdisk/bin
install -s ash.BOOT $RPM_BUILD_ROOT/usr/lib/bootdisk/bin/ash
ln -s ash $RPM_BUILD_ROOT/usr/lib/bootdisk/bin/sh
%endif

# other
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}
install sh $RPM_BUILD_ROOT%{_bindir}/ash
install ash.static $RPM_BUILD_ROOT%{_bindir}/ash.static
install sh.1 $RPM_BUILD_ROOT%{_mandir}/man1/ash.1
echo ".so ash.1" > $RPM_BUILD_ROOT%{_mandir}/man1/bsh.1
ln -sf ash $RPM_BUILD_ROOT/%{_bindir}/bsh

%post
if [ ! -f /etc/shells ]; then
        echo "%{_bindir}/ash" > /etc/shells
        echo "%{_bindir}/bsh" >> /etc/shells
else
        if ! grep '^%{_bindir}/ash$' /etc/shells > /dev/null; then
                echo "%{_bindir}/ash" >> /etc/shells
        fi
        if ! grep '^%{_bindir}/bsh$' /etc/shells > /dev/null; then
                echo "%{_bindir}/bsh" >> /etc/shells
        fi
fi

%post static
if [ ! -f /etc/shells ]; then
        echo "%{_bindir}/ash.static" >> /etc/shells
else
        if ! grep '^%{_bindir}/ash.static$' /etc/shells > /dev/null; then
                echo "%{_bindir}/ash.static" >> /etc/shells
        fi
fi

%preun
if [ "$0" = 0 ]; then
        grep -v %{_bindir}/ash /etc/shells | grep -v %{_bindir}/bsh | grep -v %{_bindir}/ash.static > /etc/shells.new
        mv -f /etc/shells.new /etc/shells
fi

%preun static
if [ "$0" = 0 ]; then
        grep -v %{_bindir}/ash /etc/shells | grep -v %{_bindir}/bsh > /etc/shells.new
        mv -f /etc/shells.new /etc/shells
fi

%verifyscript
for n in ash bsh ash.static; do
    echo -n "Looking for $n in /etc/shells... "
    if ! grep "^%{_bindir}/${n}\$" /etc/shells > /dev/null; then
	echo "missing"
	echo "${n} missing from /etc/shells" >&2
    else
	echo "found"
    fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ash
%attr(755,root,root) %{_bindir}/bsh
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ash.static

%if %{?BOOT:1}%{!?BOOT:0}
%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/bootdisk/bin/*
%endif
