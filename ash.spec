Summary:     Small bourne shell from Berkeley
Summary(de): Kleine Bourne-Shell von Berkeley
Summary(fr): Shell Bourne réduit de Berkeley
Summary(pl): Ma³y shell bourne'a 
Summary(tr): Ufak bir bourne kabuðu
Name:        ash
Version:     0.2
Release:     14
Copyright:   BSD
Group:       Shells
Source:      ftp://sunsite.unc.edu:/pub/Linux/system/shells/ash-linux-%{version}.tar.gz
Patch:       ash-make.patch
Prereq:      fileutils, grep
Buildroot:   /tmp/%{name}-%{version}-root
Conflicts:   mkinitrd <= 1.7

%description
ash is a bourne shell clone from Berkeley.  It supports all of the standard
Bourne shell commands and has the advantage of supporting them while 
remaining considerably smaller than bash. 

%description -l de
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle Standard-Bourne-Shell-
Befehle unterstützt und dennoch erheblich weniger Platz beansprucht als bash. 

%description -l fr
ash est un clone Berkeley du shell Bourne. Il gère toutes les commandes
standard du shell Bourne et a l'avantage de les gérer tout en restant
considérablement plus petit que bash.

%description -l pl
Ash jest klonem shell'a bourne'a z Berkely. Obs³uguje standardowe komendy
shell'a Bourne'a i jest mniejszy ni¿ bash. 

%description -l tr
ash, Berkeley'in bir bourne kabuðu kopyasýdýr. Standart bourne kabuðu
komutlarýnýn tümünü destekler ve bash kabuðundan daha küçük olma
avantajýna sahiptir.

%prep
%setup -q -n ash-linux-%{version}
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,usr/man/man1}

install -s sh $RPM_BUILD_ROOT/bin/ash
install sh.1 $RPM_BUILD_ROOT/usr/man/man1/ash.1
echo ".so ash.1" > $RPM_BUILD_ROOT/usr/man/man1/bsh.1
ln -sf ash $RPM_BUILD_ROOT/bin/bsh

rm -f sh
make STATIC=-static

install -s sh $RPM_BUILD_ROOT/bin/ash.static

%post
if [ ! -f /etc/shells ]; then
	echo "/bin/ash" > /etc/shells
	echo "/bin/bsh" >> /etc/shells
else
	if ! grep '^/bin/ash$' /etc/shells > /dev/null; then
		echo "/bin/ash" >> /etc/shells
	fi
	if ! grep '^/bin/bsh$' /etc/shells > /dev/null; then
		echo "/bin/bsh" >> /etc/shells
	fi
fi

%postun
if [ "$0" = 0 ]; then
	grep -v '^/bin/ash' < /etc/shells | grep -v '^/bin/bsh' > /etc/shells.new
	mv /etc/shells.new /etc/shells
fi

%verifyscript
for n in ash bsh; do
    echo -n "Looking for $n in /etc/shells... "
    if ! grep "^/bin/${n}\$" /etc/shells > /dev/null; then
	echo "missing"
	echo "${n} missing from /etc/shells" >&2
    else
	echo "found"
    fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /bin/*
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
  [0.2-14]
- updated to correct path on SunSITE.

* Sun Sep 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2-13]
- added -q %setup parameter,
- simplification in %install,
- bsh(1) man page is now maked as nroff include to ash(1) instead
  making sym link to ash.1 (this allow compress man pages in future).

* Mon Jun 29 1998 Wojtek Slusarczyk <wojtek@shadow.eu.org>
- added pl translation.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- made /bin/ash built shared
- added ash.static
- uses a buildroot and %attr

* Sun Aug 24 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- statically linked

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- fixed preinstall script to >> /etc/shells for bsh.
